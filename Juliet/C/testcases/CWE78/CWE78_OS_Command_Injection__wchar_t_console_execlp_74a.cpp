/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE78_OS_Command_Injection__wchar_t_console_execlp_74a.cpp
Label Definition File: CWE78_OS_Command_Injection.strings.label.xml
Template File: sources-sink-74a.tmpl.cpp
*/
/*
 * @description
 * CWE: 78 OS Command Injection
 * BadSource: console Read input from the console
 * GoodSource: Fixed string
 * Sinks: execlp
 *    BadSink : execute command with wexeclp
 * Flow Variant: 74 Data flow: data passed in a map from one function to another in different source files
 *
 * */

#include "std_testcase.h"
#include <map>

#include <wchar.h>

#ifdef _WIN32
#define COMMAND_INT_PATH L"%WINDIR%\\system32\\cmd.exe"
#define COMMAND_INT L"cmd.exe"
#define COMMAND_ARG1 L"/c"
#define COMMAND_ARG2 L"dir "
#define COMMAND_ARG3 data
#else /* NOT _WIN32 */
#include <unistd.h>
#define COMMAND_INT_PATH L"/bin/sh"
#define COMMAND_INT L"sh"
#define COMMAND_ARG1 L"-c"
#define COMMAND_ARG2 L"ls "
#define COMMAND_ARG3 data
#endif

using namespace std;

namespace CWE78_OS_Command_Injection__wchar_t_console_execlp_74
{

#ifndef OMITBAD

/* bad function declaration */
void badSink(map<int, wchar_t *> dataMap);

void bad()
{
    wchar_t * data;
    map<int, wchar_t *> dataMap;
    wchar_t dataBuffer[100] = COMMAND_ARG2;
    data = dataBuffer;
    {
        /* Read input from the console */
        size_t dataLen = wcslen(data);
        /* if there is room in data, read into it from the console */
        if (100-dataLen > 1)
        {
            /* POTENTIAL FLAW: Read data from the console */
            if (fgetws(data+dataLen, (int)(100-dataLen), stdin) != NULL)
            {
                /* The next few lines remove the carriage return from the string that is
                 * inserted by fgetws() */
                dataLen = wcslen(data);
                if (dataLen > 0 && data[dataLen-1] == L'\n')
                {
                    data[dataLen-1] = L'\0';
                }
            }
            else
            {
                printLine("fgetws() failed");
                /* Restore NUL terminator if fgetws fails */
                data[dataLen] = L'\0';
            }
        }
    }
    /* Put data in a map */
    dataMap[0] = data;
    dataMap[1] = data;
    dataMap[2] = data;
    badSink(dataMap);
}

#endif /* OMITBAD */

#ifndef OMITGOOD

/* good function declarations */

/* goodG2B uses the GoodSource with the BadSink */
void goodG2BSink(map<int, wchar_t *> dataMap);

static void goodG2B()
{
    wchar_t * data;
    map<int, wchar_t *> dataMap;
    wchar_t dataBuffer[100] = COMMAND_ARG2;
    data = dataBuffer;
    /* FIX: Append a fixed string to data (not user / external input) */
    wcscat(data, L"*.*");
    /* Put data in a map */
    dataMap[0] = data;
    dataMap[1] = data;
    dataMap[2] = data;
    goodG2BSink(dataMap);
}

void good()
{
    goodG2B();
}

#endif /* OMITGOOD */

} /* close namespace */

/* Below is the main(). It is only used when building this testcase on
 * its own for testing or for building a binary to use in testing binary
 * analysis tools. It is not used when compiling all the testcases as one
 * application, which is how source code analysis tools are tested.
 */

#ifdef INCLUDEMAIN

using namespace CWE78_OS_Command_Injection__wchar_t_console_execlp_74; /* so that we can use good and bad easily */

int main(int argc, char * argv[])
{
    /* seed randomness */
    srand( (unsigned)time(NULL) );
#ifndef OMITGOOD
    printLine("Calling good()...");
    good();
    printLine("Finished good()");
#endif /* OMITGOOD */
#ifndef OMITBAD
    printLine("Calling bad()...");
    bad();
    printLine("Finished bad()");
#endif /* OMITBAD */
    return 0;
}

#endif
