# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.6

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.6.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.6.1/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/build

# Include any dependencies generated for this target.
include CMakeFiles/lengthOfLongestSubstring.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/lengthOfLongestSubstring.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/lengthOfLongestSubstring.dir/flags.make

CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o: CMakeFiles/lengthOfLongestSubstring.dir/flags.make
CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o: ../length_of_longest_substring.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o -c /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/length_of_longest_substring.cpp

CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/length_of_longest_substring.cpp > CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.i

CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/length_of_longest_substring.cpp -o CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.s

CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o.requires:

.PHONY : CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o.requires

CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o.provides: CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o.requires
	$(MAKE) -f CMakeFiles/lengthOfLongestSubstring.dir/build.make CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o.provides.build
.PHONY : CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o.provides

CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o.provides.build: CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o


# Object files for target lengthOfLongestSubstring
lengthOfLongestSubstring_OBJECTS = \
"CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o"

# External object files for target lengthOfLongestSubstring
lengthOfLongestSubstring_EXTERNAL_OBJECTS =

lengthOfLongestSubstring: CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o
lengthOfLongestSubstring: CMakeFiles/lengthOfLongestSubstring.dir/build.make
lengthOfLongestSubstring: utils/libutils.a
lengthOfLongestSubstring: CMakeFiles/lengthOfLongestSubstring.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable lengthOfLongestSubstring"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/lengthOfLongestSubstring.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/lengthOfLongestSubstring.dir/build: lengthOfLongestSubstring

.PHONY : CMakeFiles/lengthOfLongestSubstring.dir/build

CMakeFiles/lengthOfLongestSubstring.dir/requires: CMakeFiles/lengthOfLongestSubstring.dir/length_of_longest_substring.cpp.o.requires

.PHONY : CMakeFiles/lengthOfLongestSubstring.dir/requires

CMakeFiles/lengthOfLongestSubstring.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/lengthOfLongestSubstring.dir/cmake_clean.cmake
.PHONY : CMakeFiles/lengthOfLongestSubstring.dir/clean

CMakeFiles/lengthOfLongestSubstring.dir/depend:
	cd /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++ /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++ /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/build /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/build /Users/air/work/Algorithms/leetcode/0003_lengthOfLongestSubstring/C++/build/CMakeFiles/lengthOfLongestSubstring.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/lengthOfLongestSubstring.dir/depend

