import typing
import argparse


def find_sum_between_min_and_max_element(input_list: typing.List[int]) -> int:
    assert len(input_list) > 1
    min_el_index = 0
    max_el_index = 0
    min_el = input_list[min_el_index]
    max_el = input_list[max_el_index]
    for index, element in enumerate(input_list):
        if element > max_el:
            max_el_index = index
            max_el = element
        if element < min_el:
            min_el_index = index
            min_el = element
    return sum(
        filter(lambda a: a < 0, input_list[max_el_index + 1:min_el_index])
    )


def main():
    parser = argparse.ArgumentParser(description="Найти сумму отрицательных элементов, расположенных между максимальным и минимальным.")
    parser.add_argument(
        "integers",
        metavar="N",
        type=int,
        nargs="+",
        help="целое число",
    )

    args = parser.parse_args()
    print(find_sum_between_min_and_max_element(args.integers))


if __name__ == "__main__":
    main()
