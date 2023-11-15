import random

class WorkoutPlan:
    @property
    def warmup_exercices(self) -> list[str]:
        return [
            "Agachamentos - 25 repetições sem peso",
            "Burpees - 20 repetições",
            "Mountain Climbers - 30 repetições",
            "Polichinelos - 50 repetições",
            "Agachamento com pulos - 15 repetições",
            "Prancha - 1 minuto",
            "Joelhos Altos - 3 minutos",
            "Corrida Estacionária - 3 minutos",
        ]

    @property
    def skill_exercices(self) -> dict:
        exercicios_calistenia = {
            "Handstand Kick Ups - Ajuda a ganhar confiança, estabelecendo uma boa entrada para o handstand.": "https://www.youtube.com/watch?v=A9BlO-Y7rMU",
            "Handstand Wall Holds - Treina seu equilíbrio, mas principalmente a força e flexibilidade do pulso e ombro.": "https://www.youtube.com/watch?v=qH3J6Y3kOHI",
            "Frog Stands - Desenvolve seu equilíbrio e a força e flexibilidade do pulso.": "https://www.youtube.com/watch?v=fAg1ZlngaMo",
            "Low Bar transition work - Reforsa o movimento de um muscle up, garantindo que a transição de abaixo para acima da barra seja suave e eficiente.": "https://www.youtube.com/watch?v=mMZMk7S2oTw",
            "Jumping Muscle Ups - Dá a sensação de um bar muscle up, permitindo que você desenvolva sua força.": "https://www.youtube.com/watch?v=-m2Joe4BjcA",
            "Pseudo Planche - Permite que você desenvolva a força e flexibilidade do pulso e ombro necessárias para uma plancha, sem precisar da extrema força do core para uma plancha completa.": "https://www.youtube.com/watch?v=odcPqBOlJhI",
            "Tuck Planche - Uma progressão a partir do Frog Stands. Isso pode ser desenvolvido ainda mais para a straddle planche.": "https://www.youtube.com/watch?v=JnG8yYyWOVQ",
            "Seated L-sits - Reduz a resistência, para que você desenvolva a força do core apenas com o peso das pernas.": "https://www.youtube.com/watch?v=E5SYskqjPqY",
            "Tucked leg Bar L-sits - A próxima progressão, pois você precisa segurar o peso do seu corpo inteiro, mas é mais fácil do que um L-sit completo.": "link9",
            "Hanging leg raise holds - Aproveita o impulso do hanging leg raise para entrar na posição de L-sit. Segurar o retorno por alguns segundos desenvolve a força estática do core.": "https://www.youtube.com/watch?v=Pr1ieGZ5atk",
        }
        return exercicios_calistenia

    @property
    def skill_exercices_list(self) -> list[str]:
        return list(self.skill_exercices.keys())

    @property
    def skill_exercices_links(self) -> list[str]:
        return list(self.skill_exercices.values())

    @property
    def workout_a(self) -> list:
        return [
            "20 Squats",
            "10 Pull-ups",
            "10 Standard Push-ups",
            "10 Hanging Leg Raises",
            "10 Burpees",
            "10 Bench Dips",
            "1 minute rest",
        ]

    @property
    def workout_b(self) -> list:
        return [
            "8 Diamond Push-ups",
            "10 Biceps Pull-ups",
            "12 Inverted Rows",
            "20 Jumping Lunges",
            "30 second Plank",
            "1 minute rest",
        ]

    @property
    def workout_c(self) -> list:
        return [
            "5 Pistol Squats on each leg",
            "5 Incline Push-ups",
            "5 Clap Push-ups",
            "5 Narrow Grip Pull-ups",
            "20 Burpees",
            "30 seconds rest",
        ]

    @property
    def workout_d(self) -> list:
        return [
            "15 Squat Jumps",
            "15 Wide Arm Push-ups",
            "15 Parallel Bar or Ring Dips",
            "15 Leg Raises",
            "10 Windshield Wipers",
            "30 seconds side plank on each side",
            "1 minute rest",
        ]

    @property
    def workout_e(self) -> list:
        return [
            "50 meter Duck Walk",
            "15 Box/Bench Jumps",
            "10 Push-ups",
            "10 Inverted Rows",
            "10 Pull-ups",
            "15 Leg Raises",
            "50 second Plank",
            "1 minute rest",
        ]

    @property
    def strength_fundamentals(self) -> list:
        return [self.workout_a, self.workout_b, self.workout_c, self.workout_d, self.workout_e]

def get_unique_elements(input_list, num_elements):
    """
    Get a specific number of unique elements from a list.

    Parameters:
    - input_list: The input list from which to select elements.
    - num_elements: The number of unique elements to retrieve.

    Returns:
    A list containing the unique elements.
    """
    # Make sure the requested number of elements is not greater than the length of the input list
    if num_elements > len(input_list):
        raise ValueError("Number of elements requested is greater than the length of the input list")

    # Use random.sample() to get unique elements
    unique_elements = random.sample(input_list, num_elements)

    return unique_elements