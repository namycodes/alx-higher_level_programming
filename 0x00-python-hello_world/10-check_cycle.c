#include "lists.h"

/**
 * check_cycle - scrutineses a linked list for containning a cycle
 * @list: list to check
 *
 * Return: 1 if list has cycle, if it does not 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
}	return (0);
