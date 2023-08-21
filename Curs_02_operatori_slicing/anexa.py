# Print line number

from inspect import currentframe, getframeinfo

cf = currentframe()
filename = getframeinfo(cf).filename

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

print('This is line, python says line ', get_linenumber())
print('This filename is ', get_linenumber())