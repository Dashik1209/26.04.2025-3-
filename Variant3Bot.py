import telebot

BOT_TOKEN = "7630446633:AAGEI9Ldey_fVc_35Q95ttIppSdoXsskSpc"
bot = telebot.TeleBot(BOT_TOKEN)

# 1. Глобальный словарь для хранения задач всех пользователей
tasks = {}  # tasks[user_id] = [task1, task2, ...]



@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Здравствуйте! Я бот для управления вашими задачами.  Используйте /addtask, /showtasks, /deltask.",
    )


# 2. Обработать команду /addtask
@bot.message_handler(commands=["addtask"])
def add_task_handler(message):
    bot.reply_to(message, "Введите текст задачи:")
    bot.register_next_step_handler(message, add_task_step)


def add_task_step(message):
    user_id = message.chat.id
    task = message.text
    if user_id not in tasks:
        tasks[user_id] = []
    tasks[user_id].append(task)
    bot.reply_to(message, f"Задача '{task}' добавлена!")


# 3. Обработать команду /showtasks
@bot.message_handler(commands=["showtasks"])
def show_tasks_handler(message):
    user_id = message.chat.id
    if user_id not in tasks or not tasks[user_id]:
        bot.reply_to(message, "Ваш список задач пуст.")
        return

    task_list = "\n".join(
        [f"{i+1}. {task}" for i, task in enumerate(tasks[user_id])]
    )
    bot.reply_to(message, f"Ваши задачи:\n{task_list}")


# 4. Обработать команду /deltask
@bot.message_handler(commands=["deltask"])
def deltask_handler(message):
    user_id = message.chat.id
    if user_id not in tasks or not tasks[user_id]:
        bot.reply_to(message, "Ваш список задач пуст.")
        return

    # a. Бот сначала показывает список задач.
    task_list = "\n".join(
        [f"{i+1}. {task}" for i, task in enumerate(tasks[user_id])]
    )
    bot.reply_to(
        message,
        f"Ваши задачи:\n{task_list}\n\nВведите номер задачи для удаления:",
    )
    bot.register_next_step_handler(message, deltask_step)


def deltask_step(message):
    user_id = message.chat.id
    try:
        task_number = int(message.text) - 1  # Нумерация с 1, индекс с 0
        if 0 <= task_number < len(tasks[user_id]):
            deleted_task = tasks[user_id].pop(task_number)
            bot.reply_to(message, f"Задача '{deleted_task}' удалена!")
        else:
            bot.reply_to(message, "Ошибка: Неверный номер задачи.")
    except ValueError:
        bot.reply_to(message, "Ошибка: Введите число (номер задачи).")


# 5. Обработать возможные ошибки (дополнительно - любые текстовые сообщения)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я понимаю только команды /addtask, /showtasks, /deltask.")


print("Бот запущен...")
bot.infinity_polling()