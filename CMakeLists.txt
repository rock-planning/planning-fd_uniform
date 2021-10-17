# CMakeLists.txt has to be located in the project folder and cmake has to be
# executed from 'project/build' with 'cmake ../'.
cmake_minimum_required(VERSION 3.9)
project(uniform
    VERSION 0.1
    DESCRIPTION "FastDownward Uniform Base Planner"
)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(Rock)
rock_init()

add_definitions(-Wno-deprecated)
add_definitions(-Wextra -Wno-sign-compare)
add_definitions(-DUSE_LP=1)
add_definitions(-DCOIN_USE_CLP=1)
add_definitions(-DSTATE_VAR_BYTES=1)

add_subdirectory(src)

