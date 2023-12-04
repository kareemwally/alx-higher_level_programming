#include "lists.h"
#include <stddef.h>
/**
 *is_palindrome :function to check symmetry
 *Description: that function checks symmetrical lists
 *@head: pointer to the base pointer of list
 *Return: (int)
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL)
{
return (1);
}
listint_t *current, *mov;
current = *head;
mov = *head;
while (current->next != NULL)
{
current = current->next;
}
while (1)
{
if (mov->n != current->n)
{
return (0);
}
mov = mov->next;
if (mov == current)
{
break;
}
current = current - 2;
}
return (1);
}
