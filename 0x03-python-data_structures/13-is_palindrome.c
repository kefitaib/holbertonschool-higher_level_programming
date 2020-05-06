#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * *reverse_listint - Reverse a list.
 * @head : first elemment in the list.
 * Return: thr new list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *l = *head, *tmp;

	if (l)
	{
		if (l->next)
		{
			*head = l->next;
			l->next = NULL;
			tmp = l;
			l = *head;

			while (l->next)
			{
				*head = l->next;
				l->next = tmp;
				tmp = l;
				l = *head;
			}
			l->next = tmp;
			*head = l;
		}
	}
	return (*head);
}


/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 * Return: 1 if the list is palindrome, 0 if not.
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *l = *head;
	int len = 0, i;

	if (!tmp || !tmp->next)
		return (1);

	for (; tmp; len++)
		tmp = tmp->next;

	tmp = *head;
	for (i = 0; i < len / 2; i++)
		tmp = tmp->next;

	tmp  = reverse_listint(&tmp);

	while (tmp)
	{
		if (l->n != tmp->n)
			return (0);

		l = l->next;
		tmp = tmp->next;
	}

	return (1);
}
