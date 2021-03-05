def cprof(sample):
    flag_brace = 0
    flag_method = 1
    flag_escape = 0
    output = ""
    method = ""
    stack = [""]
    for i in sample:
        output += i
        if i == "#":
            flag_escape = 1
        if flag_escape == 0:
            stack[len(stack) - 1] += i
        if i == "\n":
            flag_escape = 0
            flag_method = 1
        if i == "{":
            flag_brace = 1
            stack.append("")
        if i == "}":
            flag_brace = 0
            flag_escape = 0
            stack.pop()
            stack[len(stack) - 1] = ""
            if len(stack) == 1:
                stack[0] = ""
        if flag_brace == 1 and flag_escape == 0:
            method = stack[len(stack) - 2]
            pos = method.find("class ")
            if pos != -1 and not(method[pos - 1].isalnum()):
                flag_method = 0
            pos = method.find("struct ")
            if pos != -1 and not(method[pos - 1].isalnum()):
                flag_method = 0
            pos = method.find("enum ")
            if pos != -1 and not(method[pos - 1].isalnum()):
                flag_method = 0
            pos = method.find("union ")
            if pos != -1 and not(method[pos - 1].isalnum()):
                flag_method = 0
            if flag_method == 1:
                method = method[max(method.rfind(i) for i in ";}") + 1: len(method) - 1]
                method = method.replace("\r", "").replace("\n", "").strip()
                output += "____debug____(\"[CALL]: " + method + "\");" + "\r\n"
            flag_brace = 0
    return output

samplec = "           \r\n\
#include <stdio.h>    \r\n\
#include \"main.h\"   \r\n\
#define sample ({})   \r\n\
#define sample2 ({ }) \r\n\
                      \r\n\
void func(int arg);   \r\n\
                      \r\n\
class a : public b    \r\n\
{                     \r\n\
public:               \r\n\
    member v = 0;     \r\n\
    a() {}            \r\n\
    ~a() {}           \r\n\
};                    \r\n\
                      \r\n\
typedef struct _s     \r\n\
{                     \r\n\
    member v = 0;     \r\n\
}   s, *ps;           \r\n\
                      \r\n\
enum enumeration      \r\n\
{                     \r\n\
    a = 1,            \r\n\
    b,                \r\n\
    c                 \r\n\
};                    \r\n\
                      \r\n\
union u_t             \r\n\
{                     \r\n\
    a = 1,            \r\n\
    b,                \r\n\
    c                 \r\n\
};                    \r\n\
                      \r\n\
 void func(int arg) { \r\n\
}                     \r\n\
                      \r\n\
 void construct (void)\r\n\
{}                    \r\n\
                      \r\n\
int main()            \r\n\
{                     \r\n\
    return 0;         \r\n\
}                     \r\n\
"

output = cprof(samplec)
print(output)

