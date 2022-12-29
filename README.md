# Catch

A simple game I am writing in raylib and python as a toolki practice for the Winter MelonJam 2022. The old codebase was wrecked b a variety of factors and rendered undistributable, so this is a second attempt.

This Game is licensed under the GNU GPL v3. Other licenses include:

|Library|License|
|-------|-------|
|raylibpyctbg (Raylib Python CTypes Bindings Generator) | MIT |

## Setting up a development toolchain:

Artix GNU/Linux is used as my primary development machine, but any GNU/Linux distribution should work well.

 * Install the `raylib` package from your distro repositories. The name may vary, but for Arch-based distros such as Manjaro or EndeavourOS, issue `pacman -S raylib` as `root`.
 * Go to the `game/rlapi` directory and edit `rlapicfg.py` to configure the path of the raylib library binary. the base directory is `/usr/lib`, so figure out relative paths yourself. all file names are prefixed with `64bit/`, so if you put `libraylib.so.420` into the constant, it will appear as `64bit/libraylib.so.420`, so keep that in mind when fumbling with relative paths.

Now, run the neccesary scripts defined in `pyproject.toml` to run, build, etc.