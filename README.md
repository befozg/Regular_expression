## Regular_expression (Формальные языки)
# Условие:
Заданы регулярное выражение alpha, буква x, натуральное число k. Вывести, есть ли в языке L(alpgh) слова, содержащие подслово x^k.

## Решение. 
Работаю с множеством слов на стэке.
Смотрим на текущий символ:
- буква/пустое слово => добавляем в стек множество из одного элемента.
- + => pop из стека два множества, сливаем их и push в стек.
- . => pop из стека два множества, добавляем множество, создаем новое множество - их декартовое произведение.
- * => pop из стека одно множество, тут несколько случаев: дополняем его пустым символом, а также, если в стеке есть слово состоящее только из буквы, которая заданна в условии, заданным префиксом. Кладем множество обратно.
    0. добавим пустое слово
    1. если слово из множества префиксов вида {x, xx, xxx, ..., x^k}, то результирующее множество - это множество {x^k, 1}
    2. если не 2, но слово начинается на x, то достаточно кидать это множество
    3. остальные слова не стоит итерировать, ибо нас интересует префикс, а инвариант по наличию префикса x^k не изменится,
    если это слова не кидать, мы просто сузим круг поиска.
Корректность алгоритма достаточно просто доказать:
рассмотрим свойство : "Есть слово с префиксом x^k на стеке <=> есть и в валидной срезке регулярки(неформально, конечно, но устно можно легче объяснить)"
push({letter}) - свойство сохраняется.
push({'+'}) - слияние не меняет инвариант, очевидно, множество слов на стеке не меняется.
push({'.'}) - эта операция сконкатенирует слова, тут свойство наше не может измениться, поскольку конкатенация - это продолжение слова, был префикс - он останется
в результирующем множестве наличие.
push({'*'}) - мы отдельно обрабатываем случай с x-префиксами, и остальные, поэтому это легальный переход.
Итого, В результирующем множестве на стеке наличие нужного префикса эквивалентно наличию в языке, задаваемом полным регулярным выражением.


Building Requirements:
-    ubuntu
-    python3.0 или выше
-    pip3
-    256mb RAM
-    venv
-    1 cpu