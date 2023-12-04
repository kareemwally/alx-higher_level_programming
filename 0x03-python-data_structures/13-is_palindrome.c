#include "lists.h"
#include <stddef.h>
/**
 *check_even -check the list if it's even
 *Description: simple function
 *@mov:pointer to 1st node
 *@current:pointer to last node
 *Return: (int)
 */
int check_even(listint_t *mov, listint_t *current)
{
while(1)
{
if (mov->n != current->n)
{
return (0);
}
mov = mov ->next;
if (mov == current)
{
break;
}
current = current - 2;
}
return (1);
}
/**
 *check_odd -function to check odd_list nodes
 *Description: simples function
 *@mov:pointer to 1st node
 *@current:pointer to last node
 *Return: (int)
 */
int check_odd(listint_t *mov, listint_t *current)
{
while(1)
{
if (mov->n != current->n)
{
return (0);
}
if (mov == current)
{
break;
}
mov = mov ->next;
current = current - 2;
}
return (1);
}
/**
 *is_palindrome :function to check symmetry
 *Description: that function to check simitric
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
int n = 1;
while(current->next != NULL)
{
current = current->next;
n++;
}
if (n % 2 == 0)
{
return (check_even(mov, current));
}
else
{
return (check_odd(mov, current));
}
return (1);
}
