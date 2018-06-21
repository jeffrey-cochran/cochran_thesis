import matlab.engine
from os import chdir as set_cwd
from os.path import dirname, join, abspath

def start_matlab():
    #
    # Set the current working directory to the matlab source directory
    python_src_dir = dirname(abspath(__file__))
    matlab_src_dir = join(dirname(python_src_dir), "matlab")
    set_cwd(matlab_src_dir)
    #
    # Start engine and run a script
    eng = matlab.engine.start_matlab()
    #
    return eng