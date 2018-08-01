def outer_function(msg):


    def inner_function():
        print (msg)
        return inner_function()

hifunc=outer_function('hi')

print hifunc
