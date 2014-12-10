# CMakeLists.txt has to be located in the project folder and cmake has to be
# executed from 'project/build' with 'cmake ../'.
cmake_minimum_required(VERSION 2.6)

find_package(Rock)
rock_init(uniform 0.1)

add_definitions(-Wno-deprecated)
add_definitions(-Wextra -Wno-sign-compare)
add_definitions(-DUSE_LP=1)
add_definitions(-DCOIN_USE_CLP=1)
add_definitions(-DSTATE_VAR_BYTES=1)

list(APPEND CMAKE_CXX_FLAGS "-std=c++11")
add_subdirectory(src)

