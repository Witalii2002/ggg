from functools import wraps


def log(filename=None):
    """Декоратор для логирования начала, результатов и ошибок функции.
    Args:
    filename (str, optional): Имя файла для записи логов. Если не указано, логи выводятся в консоль."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Функция-обертка для выполнения логирования."""
            function_name = func.__name__

            log_message = ""  # Initialize here
            try:
                result = func(*args, **kwargs)
                log_message = f"{function_name} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_type = type(e).__name__
                # inspect.signature(func).parameters
                # inspect.getcallargs(func, *args, **kwargs) # deprecated
                log_message = f"{function_name} error: {error_type}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                raise  # Re-raise the exception
            finally:
                pass  # Removed end of finction call.

        return wrapper

    return decorator
