# cprof
C-Profiler, a batch tool that scans C source code and conditionally adds debug statements to every method

## Disclaimer: This script is alpha-quality software. There are too many known bugs to note and will likely not work on non-standard code.

![Image of cprof](https://github.com/TheMindVirus/cprof/blob/main/cprof.png)

The script adds `____debug____("[CALL]: <method-name>");` statements to every scope that the script considers to be a method.
This detection is in its infancy and may not find everything correctly.
It is up to the developer building the software to determine the implementation of the `____debug____()` function.

Alternatively, there are `gcc` tools and the `-pg` option to generate output for GNU `gprof` where that is available to use.
The end goal is to be able to debug the linux kernel and add debug statements to the first line of every method block,
without interrupting time-critical activities. Another way to do this is by using `openocd` via JTAG, `gdb` and stepwise function call counting.

The log file and the result of the function call counting can be used to filter out and prune the source tree,
so that only necessary and efficient code remains. This may make it easier to identify functional mechanisms from non-functional issues.
It is also the responsibility of the developer to maintain standard code layout, otherwise it will be difficult for the machine to parse.
