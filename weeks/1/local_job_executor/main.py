import executor
import jobs


def main() -> None:
    with executor.LocalJobExecutor() as sync_ex:
        for i in range(1, 11):
            if i % 2 == 0:
                sync_ex.submit(jobs.sync_sj, i)
            else:
                sync_ex.submit(jobs.sync_sj, "fail me")

        sync_ex.start()


if __name__ == "__main__":
    main()
