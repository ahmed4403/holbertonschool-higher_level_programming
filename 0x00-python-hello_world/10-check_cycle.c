#include "lists.h"
/**
 * check_cycle - check if there's a cycle
 * @list: head
 * Return: either one or zero
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL)
		return (0);
	tmp = list;
	while (tmp->next && tmp)
	{
		tmp = tmp->next;
		if (tmp->next == list)
			return (1);
	}
	return (0);
}
