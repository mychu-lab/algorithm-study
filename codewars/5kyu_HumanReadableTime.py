'''https://www.codewars.com/kata/52685f7382004e774f0001f7'''
def make_readable(seconds):
    return str('{0:02d}'.format(seconds//3600))+':'+str('{0:02d}'.format((seconds%3600)//60))+':'+str('{0:02d}'.format((seconds%3600)%60))