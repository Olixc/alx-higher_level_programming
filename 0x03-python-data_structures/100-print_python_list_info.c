#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
    int i, size, alloc;
    PyObject *obj;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);
    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}
