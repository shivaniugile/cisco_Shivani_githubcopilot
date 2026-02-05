"""Armstrong (Narcissistic) number utilities.

This module provides functions to check whether a number is an Armstrong
number and to generate Armstrong numbers up to a limit. An Armstrong number
in a given base is equal to the sum of its digits each raised to the power
of the number of digits.

Examples (base 10): 0, 1, 153, 370, 371, 407.

Design goals:
- Clear API with type hints.
- Robust input validation.
- Simple CLI for quick checks and listing.

Time complexity:
- `is_armstrong(n)`: O(k) where k is the number of digits of `n` in the
  selected base.
- `generate_armstrong(limit)`: O(limit * k) in the worst case, where k is the
  digit count per number.
"""

from __future__ import annotations

from typing import List, Optional, Sequence
import argparse


def _digits(n: int, base: int) -> List[int]:
	"""Return the digits of `n` in `base` (least significant first).

	Parameters
	----------
	n: int
		Non-negative integer to convert.
	base: int
		Numerical base; must be >= 2.

	Returns
	-------
	List[int]
		Digits of `n` in the given base, least significant first.
	"""
	if n < 0:
		raise ValueError("n must be non-negative")
	if base < 2:
		raise ValueError("base must be >= 2")

	if n == 0:
		return [0]

	digits: List[int] = []
	m = n
	while m > 0:
		digits.append(m % base)
		m //= base
	return digits


def is_armstrong(n: int, base: int = 10) -> bool:
	"""Return True if `n` is an Armstrong number in `base`.

	The check computes the sum of each digit raised to the power of the
	number of digits (in the given base) and compares it to `n`.

	Parameters
	----------
	n: int
		Non-negative integer to check.
	base: int, default 10
		Numerical base; must be >= 2.

	Returns
	-------
	bool
		True if `n` is an Armstrong number, else False.
	"""
	if n < 0:
		return False
	digits = _digits(n, base)
	k = len(digits)
	total = sum(d ** k for d in digits)
	return total == n


def generate_armstrong(limit: int, base: int = 10) -> List[int]:
	"""Generate Armstrong numbers in `[0, limit)` in the given base.

	Parameters
	----------
	limit: int
		Upper bound (exclusive). Must be >= 0.
	base: int, default 10
		Numerical base; must be >= 2.

	Returns
	-------
	List[int]
		List of Armstrong numbers in the interval.
	"""
	if limit < 0:
		raise ValueError("limit must be >= 0")
	if base < 2:
		raise ValueError("base must be >= 2")
	return [n for n in range(limit) if is_armstrong(n, base)]


def _parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Armstrong number utilities",
	)
	subparsers = parser.add_subparsers(dest="command", required=True)

	check_p = subparsers.add_parser("check", help="Check if a number is Armstrong")
	check_p.add_argument("n", type=int, help="Number to check (non-negative)")
	check_p.add_argument("--base", type=int, default=10, help="Numerical base (>=2)")

	list_p = subparsers.add_parser("list", help="List Armstrong numbers up to limit")
	list_p.add_argument("limit", type=int, help="Upper bound (exclusive)")
	list_p.add_argument("--base", type=int, default=10, help="Numerical base (>=2)")

	return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
	"""CLI entry point for quick checks and listing."""
	args = _parse_args(argv)

	if args.command == "check":
		n: int = args.n
		base: int = args.base
		try:
			result = is_armstrong(n, base)
		except ValueError as e:
			print(f"error: {e}")
			return 2
		if result:
			print(f"{n} is an Armstrong number (base {base}).")
			return 0
		print(f"{n} is NOT an Armstrong number (base {base}).")
		return 1

	if args.command == "list":
		limit: int = args.limit
		base: int = args.base
		try:
			nums = generate_armstrong(limit, base)
		except ValueError as e:
			print(f"error: {e}")
			return 2
		print(" ".join(str(x) for x in nums))
		return 0

	return 2


if __name__ == "__main__":
	raise SystemExit(main())
