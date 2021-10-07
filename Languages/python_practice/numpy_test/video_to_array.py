from PIL import Image
import skvideo.io
import numpy as np
import torch

def load_image(imfile):
    """ Load image file as numpy array then convert to torch tensor.
    
    Args:
        imfile -- str --: Image file name.
    
    Returns:
        img -- C x H x W -- torch.tensor() float: Image in 2D tensor.
    """
    img = np.array(Image.open(imfile)).astype(np.int8)
    print("Shape of numpy array (H, W, C): ", img.shape)
    img = torch.from_numpy(img).permute(2, 0, 1)
    print("Size of torch tensor (C, H, W): ", img.size())
    return img

def load_video(vidfile):
    """ Load video file as numpy array then convert to torth tensor.
    
    Args:
        vidfile -- str --: Video file name.
    
    Returns:
        vid -- T x C x H x W -- float: Video in 3D tensor.
    """
    vid = skvideo.io.vread(vidfile)
    print("Shape of numpy array (F, H, W, C): ", vid.shape)
    vid = torch.from_numpy(vid).permute(0, 3, 1, 2)
    print("Size of torch tensor (F, C, H, W): ", vid.size())
    return vid

def main():
    print("load_image()")
    img = load_image(r"D:\Pictures\Profile_Photo-Junkeun_Park.jpg")
    print("img[None].size(): ", img[None].size())
    print("load_video()")
    #vid = load_video(r"D:\DevPath\WLASL\start_kit\raw_videos\__bh7QCaDsw.mp4")
    vid = load_video(r"D:\DevPath\WLASL\start_kit\raw_videos\14014.swf")
    print("vid[0].size(): ", vid[0].size())


if __name__ == "__main__":
    main()