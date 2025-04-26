def print_dates_with_diff():
    data = [
        ("1945-08-17", 27209),
        ("1785-11-11", 85561),
        ("1783-06-08", 86448),
        ("1889-05-02", 47769),
    ]

    for date_str, diff_days in data:
        print(f"{date_str} 00:00:00 selisih {diff_days} hari")

print_dates_with_diff()