#include "lists.h"
#include <stdio.h>
/**
 * insert_node - check the code for
 * @head: start of linked list
 * @number: new integer
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr = *head, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		return (new);
	if (ptr->next == NULL)
	{
		if (ptr->n < number)
		{
			(*head)->next = new;
			return (new);
		}
		new->next = *head;
		*head = new;
		return (new);
	}
	while (ptr->next)
	{
		if (ptr->n < number)
		{
			if (ptr->next->n > number)
				prev = ptr;
			ptr = ptr->next;
			continue;
		}
		new->next = ptr;
		prev->next = new;
		break;
	}
	return (new);
}
