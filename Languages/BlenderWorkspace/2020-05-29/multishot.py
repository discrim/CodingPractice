"""
Author: Junkeun Park, junkeunp@umich.edu

Log
2020-05-31 Sun: Final version
2020-05-29 Fri: Initial commit

Description
Proof of concept for
1. making camera track a target (i.e. always look at the target) - do_track()
2. moving camera to given multiple locations
3. rendering still image at every camera location
Note that the light is stationary.
"""

def capture_from_locations(cam, target, loc_list):
    """
    Move camera among each locations in the list and take photos of the target.
    INPUT
        cam -- object --
            Camera object.
        target -- object --
            Object that you want to take a picture of.
        loc_list: -- N-element list --
            List of N locations.
            Each locations are cartesian coordinates in 3-tuple, i.e. (x, y, z),
            so loc_list is [(x1, y1, z1), (x2, y2, z2), ... ]
    """
    import bpy
    
    filename = 0    # For simplicity, file names are just integers.
    
    do_track(tracker=cam, trackee=target)
    
    for loc_current in loc_list:
        cam.location = loc_current  # Move camera
        filename += 1               # Increase file name after moving
        render_image(str(filename)) # Render still image


def sphere_grid_spherical(center, radii, azis, pols):
    """
    Return spherical grid with given lists of
    radii, azimuthal angles, and polar angles.
    Note that the adjacent vertices are not equally spaced.
    INPUT
        center -- 3-tuple --
            Cartesian coordinates of the center of the sphere.
        radii -- r-element list --
            List of radii.
            E.g. [1, 2, 3]
        azis -- a-element list --
            List of azimuthal angles.
            E.g. [0, 0.5 * pi, pi, 1.5 * pi]
        pols -- p-element list --
            List of polar angles. Excluding 0 and pi is recommended.
            E.g. [0.25 * pi, 0.5 * pi, 0.75 * pi]
    OUTPUT
        grid -- (r * a * p)-element list --
            Each element is a 3-tuple of (radius, azimuthal_angle, polar_angle).
    """
    from math import pi, sin, cos
    from numpy import zeros
    
    count = 0
    grid = zeros(len(radii) * len(azis) * len(pols), dtype=tuple)
    for  rr in radii:
        for theta in azis:
            for phi in pols:
                location = (rr * sin(phi) * cos(theta) + center[0],
                            rr * sin(phi) * sin(theta) + center[1],
                            rr * cos(phi) + center[2])
                grid[count] = location
                count += 1
    return grid


def do_track(tracker, trackee):
    """
    Make the tracker track the trackee.
    e.g. do_track(camera, monkey) # Camera always sees monkey.
    """
    import bpy
    tracker.select_set(True)
    trackee.select_set(True)
    bpy.context.view_layer.objects.active = trackee # Set trackee to be tracked
    bpy.ops.object.track_set(type='TRACKTO')


def render_image(filename, format='PNG'):
    """
    Render the camera view as image. It is saved where this .blend file exists.
    INPUT
        filename: str
            Name of image file being saved without file extnesion.
            e.g. Good: my_pic / Bad: my_pic.png
        format: str
            Image format to use. Default: 'PNG'    
    """
    from pathlib import Path
    import bpy
    savedir = Path(__file__).parents[1] # Directory Where .blend file lies in
    fullpath = str(savedir) + '/' + filename
    bpy.data.scenes["Scene"].render.use_file_extension = True # Automatically adds extension
    bpy.data.scenes["Scene"].render.image_settings.file_format = format # Set image format
    bpy.data.scenes["Scene"].render.filepath = fullpath # Merge to get full path
    bpy.ops.render.render(write_still=True)


if __name__ == '__main__':

    from math import pi
    import bpy
    from numpy import arange
    
    radii = [6]
    azis = arange(0, 2 * pi, pi / 3)            # [0, 60, 120, 180, 240, 300] deg
    pols = arange(pi / 6, (5/6) * pi, pi / 6)   # [30, 60, 90, 120, 150] deg
    
    center = (1, 1, 1)
    grid = sphere_grid_spherical(center, radii, azis, pols)
    
    cam = bpy.data.objects['Camera']
    target = bpy.data.objects['Suzanne']        # Change if you use another target object
    capture_from_locations(cam, target, grid)