class ProcessedNumber:
    def __init__(self, numbers):

        self.processed = [n ** 2 for n in numbers if n % 2 == 0]

    def __str__(self):
        return f"Processed numbers: {self.processed}"

numbers = [1, 2, 3, 4, 5, 6]
processor = ProcessedNumber(numbers)

print(processor)
