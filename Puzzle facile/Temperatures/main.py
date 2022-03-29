input()
print(
    min(
        sorted([int(i) for i in input().split() or [0]], reverse=True),
        key=lambda x: abs(x),
    )
)
