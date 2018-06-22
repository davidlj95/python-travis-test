#!/bin/sh
# Runs the specificated tests
# Specify the test to run using the $TEST_SUITE environment variable
# If no variable $TEST_SUITE is found, or if it is empty, all tests will be
# run
# 
# Available tests: "tests", "style"

# Python unittests
if [ -z "$TEST_SUITE" ] || [ "$TEST_SUITE" = "tests" ]; then
	python -m unittest discover tests
fi

# Python style check
if [ -z "$TEST_SUITE" ] || [ "$TEST_SUITE" = "style" ]; then
	python -m flake8 bitcoin tests
fi
