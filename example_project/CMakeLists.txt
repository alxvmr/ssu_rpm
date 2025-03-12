cmake_minimum_required(VERSION 3.5.0)
project(my_hello VERSION 0.1.0 LANGUAGES C)

find_package (PkgConfig REQUIRED)
pkg_check_modules (GLIB REQUIRED glib-2.0)

add_executable(${CMAKE_PROJECT_NAME} main.c)

target_include_directories (${CMAKE_PROJECT_NAME} PRIVATE ${GLIB_INCLUDE_DIR})
target_link_libraries (${CMAKE_PROJECT_NAME} PRIVATE ${GLIB_LIBRARIES})
target_compile_options (${CMAKE_PROJECT_NAME} PRIVATE ${GLIB_CFLAGS})

install (TARGETS ${CMAKE_PROJECT_NAME}
         DESTINATION /usr/bin)