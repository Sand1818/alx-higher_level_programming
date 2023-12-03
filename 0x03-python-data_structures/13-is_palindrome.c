#include "lists.h"
#include <stddef.h>

/**
 * checkPalindrome - checks if a singly linked list is a palindrome
 * @left: node
 * @right: node
 * Return: 1 (palindrome), 0 (not)
 */

int checkPalindrome(listint_t **left, listint_t *right)
{
	int sand = 0;

	if (right == NULL)
		return (1);

	sand = checkPalindrome(left, right->next) &&
		((*left)->n == right->n);
	(*left) = (*left)->next;

	return (sand);
}

/**
 * is_palindrome - callfunction
 * @head: head of list
 * Return: 1 (palindome), 0 (not)
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	return (checkPalindrome(&(*head), *head));
}
