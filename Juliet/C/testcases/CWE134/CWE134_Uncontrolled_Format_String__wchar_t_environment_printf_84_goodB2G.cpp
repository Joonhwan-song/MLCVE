/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE134_Uncontrolled_Format_String__wchar_t_environment_printf_84_goodB2G.cpp
Label Definition File: CWE134_Uncontrolled_Format_String.label.xml
Template File: sources-sinks-84_goodB2G.tmpl.cpp
*/
/*
 * @description
 * CWE: 134 Uncontrolled Format String
 * BadSource: environment Read input from an environment variable
 * GoodSource: Copy a fixed string into data
 * Sinks: printf
 *    GoodSink: wprintf with "%s" as the first argument and data as the second
 *    BadSink : wprintf with only data as an argument
 * Flow Variant: 84 Data flow: data passed to class constructor and destructor by declaring the class object on the heap and deleting it after use
 *
 * */
#ifndef OMITGOOD

#include "std_testcase.h"
#include "CWE134_Uncontrolled_Format_String__wchar_t_environment_printf_84.h"

#define ENV_VARIABLE L"ADD"

#ifdef _WIN32
#define GETENV _wgetenv
#else
#define GETENV getenv
#endif

namespace CWE134_Uncontrolled_Format_String__wchar_t_environment_printf_84
{
CWE134_Uncontrolled_Format_String__wchar_t_environment_printf_84_goodB2G::CWE134_Uncontrolled_Format_String__wchar_t_environment_printf_84_goodB2G(wchar_t * dataCopy)
{
    data = dataCopy;
    {
        /* Append input from an environment variable to data */
        size_t dataLen = wcslen(data);
        wchar_t * environment = GETENV(ENV_VARIABLE);
        /* If there is data in the environment variable */
        if (environment != NULL)
        {
            /* POTENTIAL FLAW: Read data from an environment variable */
            wcsncat(data+dataLen, environment, 100-dataLen-1);
        }
    }
}

CWE134_Uncontrolled_Format_String__wchar_t_environment_printf_84_goodB2G::~CWE134_Uncontrolled_Format_String__wchar_t_environment_printf_84_goodB2G()
{
    /* FIX: Specify the format disallowing a format string vulnerability */
    wprintf(L"%s\n", data);
}
}
#endif /* OMITGOOD */
