class Factory(object):
    def __init__(self):
        self.listFigures = []

    def create_triangle(self, id, a, b, c):
        self.listFigures.append(Triangle(id, a, b, c))

    def create_rectangle(self, id, a, b, c, d):
        self.listFigures.append(Rectangle(id, a, b, c, d))

    def delete_figure(self, id):
        self.listFigures.remove(self.choose_figure(id))

    def choose_figure(self, id):
        for figure in self.listFigures:
            if id == figure.id:
                return figure

    def area(self, A, B, C):
        return (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x)

    def check_point(self, a, b, c, d):
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return max(a, c) <= min(b, d)

    def cross_line(self, A, B, C, D):
        return self.check_point(A.x, B.x, C.x, D.x) and self.check_point(A.y, B.y, C.y, D.y) and self.area(A, B, C) * \
               self.area(A, B, D) <= 0 and self.area(C, D, A) * self.area(C, D, B) <= 0

    def number_of_ribs(self, figure):
        if isinstance(figure, Triangle):
            return [[figure.pointA, figure.pointB], [figure.pointB, figure.pointC], [figure.pointC, figure.pointA]]
        else:
            return [[figure.pointA, figure.pointB], [figure.pointB, figure.pointC], [figure.pointC, figure.pointD], [figure.pointD, figure.pointA]]

    def check_cross(self, id1, id2):
        figure1 = self.choose_figure(id1)
        figure2 = self.choose_figure(id2)
        listRibs1 = self.number_of_ribs(figure1)
        listRibs2 = self.number_of_ribs(figure2)

        for rib1 in listRibs1:
            for rib2 in listRibs2:
                if self.cross_line(rib1[0], rib1[1], rib2[0], rib2[1]):
                    print(True)
                    return
        print(False)
        return

    def show_all(self):
        for figure in self.listFigures:
            figure.show()

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_point(self, x, y):
        self.x += x
        self.y += y

    def show_point(self):
        print(f"x={self.x}, y={self.y}")


class Triangle(object):
    def __init__(self, id, pointA, pointB, pointC):
        self.id = id
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC

    def move(self, x, y):
        self.pointA.move_point(x, y)
        self.pointB.move_point(x, y)
        self.pointC.move_point(x, y)

    def show(self):
        print(f"\nid: {self.id}")
        print("A:", end=" ")
        self.pointA.show_point()
        print("B:", end=" ")
        self.pointB.show_point()
        print("C:", end=" ")
        self.pointC.show_point()


class Rectangle(Triangle):
    def __init__(self, id, pointA, pointB, pointC, pointD):
        super().__init__(id, pointA, pointB, pointC)
        self.pointD = pointD

    def move(self, x, y):
        super().move(x, y)
        self.pointD.move_point(x, y)

    def show(self):
        super().show()
        print("D:", end=" ")
        self.pointD.show_point()


def main():
    factory = Factory()
    factory.create_triangle("t1", Point(1, 1), Point(3, 1), Point(2, 2))
    factory.create_rectangle("r1", Point(2, 2), Point(2, 4), Point(5, 4), Point(5, 2))
    ##factory.choose_figure("t1").move(1, 1)
    #factory.choose_figure("t1").show()
    #factory.check_cross("t1", "r1")
    while True:
        work = input(
            "Введите 1, если хотите добавить фигуру!\nВведите 2, если хотите удалить фигуру!\nВведите 3, если хотите "
            "проверить пересечение фигур!\nВведите 4, если хотите передвинуть фигуру!\nВведите 5, если хотите вывести "
            "список всех фигур!\nВведите 6, если хотите вывести одну фигуру!\nВведите любой символ, если хотите "
            "выйти!\n")
        if work == "1":
            work = input("Введите 1, если хотите добавить треугольник!\nВведите 2, если хотите добавить "
                         "прямоугольник!\n")
            id = input("Введите id фигуры:")
            while True:
                try:
                    x1 = int(input("Введите x1: "))
                    y1 = int(input("Введите y1: "))
                    x2 = int(input("Введите x2: "))
                    y2 = int(input("Введите y2: "))
                    x3 = int(input("Введите x3: "))
                    y3 = int(input("Введите y3: "))
                    break
                except ValueError:
                    print("Введите корректные значения!")
            if work == "1":
                factory.create_triangle(id, Point(x1, y1), Point(x2, y2), Point(x3, y3))
            if work == "2":
                while True:
                    try:
                        x4 = int(input("Введите x4: "))
                        y4 = int(input("Введите y4: "))
                        break
                    except ValueError:
                        print("Введите корректные значения!")
                factory.create_rectangle(id, Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))
        elif work == "2":
            while True:
                try:
                    id = input("Введите id фигуры, которую хотите удалить: ")
                    factory.delete_figure(id)
                    break
                except ValueError:
                    print("Введите корректные значения!")
        elif work == "3":
            while True:
                try:
                    id1 = input("Введите id фигуры 1: ")
                    id2 = input("Введите id фигуры 2: ")
                    factory.check_cross(id1, id2)
                    break
                except ValueError:
                    print("Введите корректные значения!")
                except AttributeError:
                    print("Введите корректные значения!")
        elif work == "4":
            while True:
                try:
                    id = input("Введите id фигуры, которую хотите передвинуть: ")
                    x, y = int(input("Введите х и у перемещения: "))
                    factory.choose_figure(id).move(x, y)
                    break
                except ValueError:
                    print("Введите корректные значения!")
                except AttributeError:
                    print("Введите корректные значения!")
        elif work == "5":
            factory.show_all()
        elif work == "6":
            while True:
                try:
                    id = input("Введите id фигуры, которую хотите вывести: ")
                    factory.choose_figure(id).show()
                    break
                except ValueError:
                    print("Введите корректные значения!")
                except AttributeError:
                    print("Введите корректные значения!")
        else:
            break


if __name__ == "__main__":
    main()
