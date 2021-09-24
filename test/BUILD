python_test(
    name = "lib_test",
    srcs = ["test.py"],
    deps = ["//src/lib:mylib"],
)

python_test(
    name = "cross_compile_test",
    srcs = ["cross_compile_test.py"],
    deps = ["//src/lib:mylib"],
)

gentest(
    name = "random_test",
    test_cmd = "plz run //src:resolve -- --package six --version 1.16.0",
    no_test_output = True,
)
