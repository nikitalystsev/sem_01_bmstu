#!/bin/bash

if [ "$(id -u)" -eq 0 ]; then
    echo "Вы действительно хотите запустить этот скрипт от имени суперпользователя? Это может быть опасно."
    exit 1
fi

if [ -e ".myconfig" ] && [ -s ".myconfig" ]; then
    echo 'Файл настроек существует и не пустой'
    file_1=".myconfigtf"
    file_2=".myconfigwf"
    file_3=".myconfiguscom"
    file_4=".myconfigwdir"
else
    echo 'Файла настроек нет. Он будет создан'
    echo ".myconfigtf\n.myconfigwf\n.myconfiguscom\n.myconfigwdir" > .myconfig
    echo ".log" > .myconfigtf
    echo ".c" > .myconfigwf
    echo "grep error* program.c>last.log" > .myconfiguscom
    echo "${PWD}" > .myconfigwdir

fi

if [ -n "$1" ] &&  [ "$1" = "-nm" ]; then
    flag=1
    shift
else
    flag=0
fi
echo "flag: " "$flag"

if [ $flag -eq 1 ] && [ "$1" -ge 1 ] && [ "$1" -le 7 ]; then
    numb1=$1
    shift
    numb2=$1
    shift
    elif [ $flag -eq 1 ] && [ "$1" -ge 8 ] && [ "$1" -le 9 ]; then
    numb1=$1
    shift
fi

echo "numb1:" "$numb1"
echo "numb2:" "$numb2"
echo "остальные_1: " "$*"



temporary_files="$(head -n 1 .myconfigtf | tail -n 1)"
echo 'временные файлы: ' "$temporary_files"
working_files="$(head -n 1 .myconfigwf | tail -n 1)"
echo 'рабочие файлы: ' "$working_files"
custom_command="$(head -n 1 .myconfiguscom | tail -n 1)"
echo 'записанная команда: ' "$custom_command"
work_folder="$(head -n 1 .myconfigwdir | tail -n 1)"
echo 'рабочая папка: ' "$work_folder"

numb_1=''
numb_2=''

BLUE="\033[36m"
VIOLET="\033[35m"
ENDCOLOR="\e[0m"

# вывод меню
menu(){
    echo -e "${VIOLET}1. Возможность просмотреть или задать заново список расширений временных файлов;
	1. Просмотреть;
	2. Задать заново.
   2. Возможность добавлять или удалять конкретное расширение из списка расширений временных файлов;
	1. Добавить;
	2. Удалить конкретное расширение.
   3. Возможность просмотреть или задать заново список расширений рабочих файлов;
	1. Просмотреть;
	2. Задать заново.
   4. Возможность добавлять или удалять конкретное расширение из списка расширений рабочих файлов;
	1. Добавить;
	2. Удалить конкретное расширение.
   5. Возможность просмотреть или задать заново рабочую папку скрипта;
	1. Просмотреть;
	2. Задать заново.
   6. Возможность удалить временные файлы.
   7. Возможность выполнить или изменить записанную команду.
   	1. Выполнить;
   	2. Изменить.
   8. Возможность просмотреть все целые числа во всех рабочих файлах с
   		указанием спецфлага: shorti для чисел от -32000 до 32000, regi для чисел
   		не-shorti от -2000000000 до 2000000000.
    9. Возможность просмотреть объём каждого временного файла${ENDCOLOR}"
}

# номер пункта меню
item_numb(){
    read -r -p "Введите номер пункта меню: " numb_1
}

# номер подпункта меню
subparagraph_numb(){
    read -r -p "Введите номер подпункта меню: " numb_2
}

# вывод расширений
output_of_files(){
    echo -e "${BLUE}Список расширений $2 файлов:${ENDCOLOR}" "$1"
}

# новые расширения файлов
new_list_of_extensions(){
    if [ $flag -eq 0 ]; then
        read -r -p "Введите новый список расширений $1 файлов через пробел: " new_list_of_extensions
        echo "$new_list_of_extensions"
    else
        echo "$*"
    fi
}

# добавление новых расширений файлов
adding_file_extensions(){
    if [ $flag -eq 0 ]; then
        read -r -p "Введите расширения для $2 файлов, которые хотите добавить через пробел: " add_extensions
        add_files="$1 $add_extensions"
        echo "$add_files"
    else
        add_files="$1 $2"
        echo "$add_files"
    fi
}

# удаление конкретного расширения из списка расширений файлов
removing_a_specific_extension_of_files(){
    if [ $flag -eq 0 ]; then
        count=1
        temp=""
        read -r -p "Введите номер удаляемого расширения: " numb_delete
        for elem in $1; do
            if [ "$count" != "$numb_delete" ]; then
                temp="$temp $elem"
            fi
            count=$((count+1))
        done
        new_files="$temp"
        echo "$new_files"
    else
        count=1
        temp=""
        for elem in $1; do
            if [ "$count" != "$*" ]; then
                temp="$temp $elem"
            fi
            count=$((count+1))
        done
        new_files="$temp"
        echo "$new_files"
    fi
}

# вывод рабочей папки скрипта
working_folder(){
    echo -e "${BLUE}Текущая рабочая директория:${ENDCOLOR}" "$1"
}

# изменение рабочей папки скрипта
change_working_folder(){
    if [ $flag -eq 0 ];then
        read -r -p "Введите расположение новой рабочей папки скрипта: " new_dir
        if [ -d "$new_dir" ]; then
            echo "$new_dir"
        fi
    else
        if [ -d "$*" ]; then
            echo "$*"

        fi
    fi
}

# удаляет временные файлы
deleting_trusted_files(){
    for elem in $temporary_files; do
        find "$work_folder" -wholename "*$elem" -type f -delete
    done
}

# вытаскивает целые числа из файла
integer_output(){
    for elem_1 in $working_files; do
        # список файлов с определенным расширением
        list_1=$(find "$work_folder" -name "*$elem_1")
        for elem_2 in $list_1; do

            # список чисел в одном файле
            list_2=$(grep -oE "[0-9]{1,}" "$elem_2")
            for elem_3 in $list_2; do
                if  [ "$elem_3" -ge -32000 ] && [ "$elem_3" -le 32000 ]; then
                    printf "%9d %8s %s\n" "$elem_3" "shorti" "$elem_2"
                    elif [ "$elem_3" -ge -2000000000 ] && [ "$elem_3" -le 2000000000 ]; then
                    printf "%9d %8s %s\n" "$elem_3" "regi" "$elem_2"
                fi
            done
        done
    done
}

# изменяет пользовательскую команду
change_custom_command(){
    if [ $flag -eq 0 ];then
        read -r -p "Введите новую пользовательскую команду: " nem_command
        echo "$nem_command"
    else
        echo "$*"
    fi
}

# показывает обьем каждого временного файла
volume_trusted_files(){
    for elem in $temporary_files; do
        # список файлов
        list=$(find "$work_folder" -wholename "*$elem" -type f)

        for elem_ in $list; do
            # список размеров файлов
            list_=$(find "$work_folder" -wholename "$elem_" -type f | wc -c)
            printf "%9d %s\n" $list_ $elem_
        done
    done
}

# основной цикл работы программы

# тихий режим
if [ $flag -eq 1 ]; then
    if [ "$numb1" = "1" ]; then

        if [ "$numb2" = "1" ]; then
            output_of_files "$temporary_files" "временных"

            elif [ "$numb2" = "2" ]; then

            echo 'переданные аргументы:' "$*"
            temporary_files=$(new_list_of_extensions "$*")
            echo "Новый список: " "$temporary_files"
            echo "$temporary_files" > .myconfigtf

        fi

        elif [ "$numb1" = "2" ]; then

        if [ "$numb2" = "1" ]; then

            echo 'переданные аргументы:' "$*"
            temporary_files=$(adding_file_extensions "$temporary_files" "$*")
            echo "Измененный список: " "$temporary_files"
            echo "$temporary_files" > .myconfigtf

            elif [ "$numb2" = "2" ]; then

            echo 'переданные аргументы:' "$*"
            temporary_files=$(removing_a_specific_extension_of_files "$*")
            echo "Измененный список: " "$temporary_files"
            echo "$temporary_files" > .myconfigtf
        fi

        elif [ "$numb1" = "3" ]; then

        if [ "$numb2" = "1" ]; then

            output_of_files "$working_files" "рабочих"

            elif [ "$numb2" = "2" ]; then

            echo 'переданные аргументы:' "$*"
            working_files=$(new_list_of_extensions "$*")
            echo "Новый список: " "$working_files"
            echo "$working_files" > .myconfigwf

        fi

        elif [ "$numb1" = "4" ]; then

        if [ "$numb2" = "1" ]; then

            echo 'переданные аргументы:' "$*"
            working_files=$(adding_file_extensions "$working_files" "$*")
            echo "Измененный список: " "$working_files"
            echo "$working_files" > .myconfigwf

            elif [ "$numb2" = "2" ]; then

            echo 'переданные аргументы:' "$*"
            working_files=$(removing_a_specific_extension_of_files "$*")
            echo "Измененный список: " "$working_files"
            echo "$working_files" > .myconfigwf

        fi

        elif [ "$numb1" = "5" ]; then

        if [ "$numb2" = "1" ]; then

            working_folder "$work_folder"

            elif [ "$numb2" = "2" ]; then

            echo 'переданные аргументы: ' "$*"
            work_folder=$(change_working_folder "$*")
            echo 'новая рабочая папка: ' "$work_folder"
            echo "$work_folder" > .myconfigwdir
        fi
        elif [ "$numb1" = "6" ]; then

        deleting_trusted_files

        elif [ "$numb1" = "7" ]; then

        if [ "$numb2" = "1" ]; then

            eval $custom_command

            elif [ "$numb2" = "2" ]; then

            custom_command=$(change_custom_command "$str_arr")
            echo "$custom_command" > .myconfiguscom
        fi
        elif [ "$numb1" = "8" ]; then

        integer_output

        elif [ "$numb1" = "9" ]; then

        volume_trusted_files

    fi

else

    menu
    item_numb
    while :
    do
        if [ "$numb_1" = "1" ]; then
            subparagraph_numb
            if [ "$numb_2" = "1" ]; then
                output_of_files "$temporary_files" "временных"
                elif [ "$numb_2" = "2" ]; then
                temporary_files=$(new_list_of_extensions "временных")
                echo "$temporary_files" > .myconfigtf
            fi

            elif [ "$numb_1" = "2" ]; then
            subparagraph_numb
            if [ "$numb_2" = "1" ]; then
                temporary_files=$(adding_file_extensions "$temporary_files" "временных")
                echo "$temporary_files" > .myconfigtf
                elif [ "$numb_2" = "2" ]; then
                temporary_files=$(removing_a_specific_extension_of_files "$temporary_files" "временных")
                echo "$temporary_files" > .myconfigtf
            fi

            elif [ "$numb_1" = "3" ]; then
            subparagraph_numb
            if [ "$numb_2" = "1" ]; then
                output_of_files "$working_files" "рабочих"
                elif [ "$numb_2" = "2" ]; then
                working_files=$(new_list_of_extensions "рабочих")
                echo "$working_files" > .myconfigwf
            fi

            elif [ "$numb_1" = "4" ]; then
            subparagraph_numb
            if [ "$numb_2" = "1" ]; then
                working_files=$(adding_file_extensions "$working_files" "рабочих")
                echo "$working_files" > .myconfigwf
                elif [ "$numb_2" = "2" ]; then
                working_files=$(removing_a_specific_extension_of_files "$working_files" "рабочих")
                echo "$working_files" > .myconfigwf
            fi

            elif [ "$numb_1" = "5" ]; then
            subparagraph_numb
            if [ "$numb_2" = "1" ]; then
                working_folder "$work_folder"
                elif [ "$numb_2" = "2" ]; then
                work_folder=$(change_working_folder)
                echo "$work_folder" > .myconfigwdir
            fi
            elif [ "$numb_1" = "6" ]; then
            deleting_trusted_files
            elif [ "$numb_1" = "7" ]; then
            subparagraph_numb
            if [ "$numb_2" = "1" ]; then
                eval $custom_command
                elif [ "$numb_2" = "2" ]; then
                custom_command=$(change_custom_command)
                echo "$custom_command" > .myconfiguscom
            fi
            elif [ "$numb_1" = "8" ]; then
            integer_output
            elif [ "$numb_1" = "9" ]; then
            volume_trusted_files
        fi

        menu
        item_numb
    done
fi
