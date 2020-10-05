mycase = 1

if mycase == 0:
    def giftbox(func):
        def inside(*args, **kwargs):
            print("Here is your gift.")
            func(*args, **kwargs)
            print("Congratulations~")
        return inside

    def gift(gift_name):
        print("It's " + gift_name)

    #mygift = giftbox(gift)
    #mygift("iPad")
    giftbox(gift("iPad"))

elif mycase == 0.1:
    def giftbox(func):
        def inside(*args, **kwargs):
            print("Here is your gift.")
            func(*args, **kwargs)
            print("Congratulations~")
        return inside

    @giftbox
    def gift(gift_name):
        print("It's " + gift_name)

    #mygift = gift
    #mygift("iPad")
    gift("iPad")

elif mycase == 1:
    # Without decorator
    def function_usage_notifier(func):
        def inner(*args, **kwargs):
            print("A function begins.")
            result = func(*args, **kwargs)
            print("A function ends.")
            return result
        return inner

    def power_self(nn):
        return nn ** nn

    myfunc = function_usage_notifier(power_self)
    print(myfunc(7))
    #print(function_usage_notifier(power_self(7))) # Not working

elif mycase == 1.1:
    # With decorator
    def function_usage_notifier(func):
        def inner(*args, **kwargs):
            print("A function begins.")
            result = func(*args, **kwargs)
            print("A function ends.")
            return result
        return inner

    @function_usage_notifier
    def power_self(nn):
        return nn ** nn

    #myfunc = power_self
    #print(myfunc(7))
    print(power_self(7))
