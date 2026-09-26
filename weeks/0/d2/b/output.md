# Примечание

Все команды подсмотрены в поиске, обычно не пользовался таким инструментарием

# Parent PID

## Команда

```shell
ps ax | grep process_demo
```

## Вывод

```terminaloutput
2077642 pts/1    Rl+    0:58 python3 process_demo.py
2077643 pts/1    R+     0:58 python3 process_demo.py
2077740 pts/0    S+     0:00 grep --color=auto process_demo
```

# Child PID

Команда использовалась та же, вывод один и тот же

# Parent/child relation

## Команда

```shell
ps j 2077643
```

## Вывод

```terminaloutput
2077642 2077643 2077642 2073395 pts/1    2077642 S+    1000   0:59 python3 process_demo.py
```

Глядя на ppid и смотря на вывод скрипта понятно их соотношение.

# Threads amount

## Команда

```shell
ps hH p <PID> | wc -l
```

## Вывод

На выходе я получил для родительского 3, а для наследника 1.

# File descriptor

Я не совсем понимаю что такое файловый дескриптор, но вот что я нашёл

## Команда

```shell
ls -lah /proc/<PID>/fd/
```

## Вывод

Для родителя

```terminaloutput
итого 0
dr-x------ 2 tecon-user tecon-user 11 сен 24 14:10 .
dr-xr-xr-x 9 tecon-user tecon-user  0 сен 24 14:10 ..
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:10 0 -> 'pipe:[51114175]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:10 1 -> 'pipe:[51114176]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:10 12 -> 'pipe:[51118635]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:10 2 -> 'pipe:[51114177]'
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:10 3 -> 'pipe:[51118631]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:10 4 -> 'pipe:[51118631]'
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:16 5 -> 'pipe:[51118632]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:10 6 -> 'pipe:[51118632]'
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:10 7 -> 'pipe:[51118633]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:10 8 -> 'pipe:[51118633]'
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:10 9 -> 'pipe:[51118634]'
```

Для наследника

```terminaloutput
итого 0
dr-x------ 2 tecon-user tecon-user 12 сен 24 14:16 .
dr-xr-xr-x 9 tecon-user tecon-user  0 сен 24 14:10 ..
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:16 0 -> 'pipe:[51114175]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:16 1 -> 'pipe:[51114176]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:16 10 -> 'pipe:[51118634]'
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:16 11 -> 'pipe:[51118635]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:16 2 -> 'pipe:[51114177]'
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:16 3 -> 'pipe:[51118631]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:16 4 -> 'pipe:[51118631]'
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:16 5 -> 'pipe:[51118632]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:16 6 -> 'pipe:[51118632]'
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:16 7 -> 'pipe:[51118633]'
l-wx------ 1 tecon-user tecon-user 64 сен 24 14:16 8 -> 'pipe:[51118633]'
lr-x------ 1 tecon-user tecon-user 64 сен 24 14:16 9 -> /dev/null
```

# Поведение при убийстве дочернего процесса

Мониторить буду с помощью ```ps ax | grep process_demo```
Обычно, если я "корректно" прерываю родительский процесс, то и он сам и дочерний процесс пропадают
После выполнения kill, в выводе команды я получил просто висящий дочерний процесс, что, вероятно и есть zombie process.
Цепочка выводов терминала:

```terminaloutput
2080184 pts/1    Rl+    0:02 python3 process_demo.py
2080185 pts/1    R+     0:02 python3 process_demo.py
2080199 pts/0    S+     0:00 grep --color=auto process_demo
```

```terminaloutput
2080185 pts/1    S      0:04 python3 process_demo.py
2080342 pts/0    S+     0:00 grep --color=auto process_demo
```