




//Библиотеки 
#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()

{
    string ans;

    do
    {

        //Объявление переменных
        int a; //переменная для выбора варианта решения
        double hyp, leg, leg2, angle;//гипотенуза,Катет,Угол
        
        //Ввод и проверка варианта решенния задачи
        cout << "Enter the digit 1 for the solution by the cosine and sin theorem or any other digit for the solution by the Pythagorean theorem  : ", cin >> a;

        while ((cin.good() != true) || (cin.peek() != '\n')) {

            cout << "\nYou have entered an invalid value\n" << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Try again =>  ";
            cout << "Enter the digit 1 for the solution by the cosine theorem or any other digit for the solution by the Pythagorean theorem ", cin >> a;
        }

        //1 первый вариант решения задачи теоремой косинусов
        if (a == 1) {
            //Ввод и проверка длины гипотенузы
            cout << "Hypotenuse = "; cin >> hyp;
            while ((cin.good() != true) || (cin.peek() != '\n') || (hyp < 0))
            {
                cout << "\nYou have entered an invalid value\n" << endl;
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cout << "Try again =>  ";
                cout << "Hypotenuse = "; cin >> hyp;
            }



            //Ввод и проверка значения угла
            cout << "Angle between hypotenuse and leg =  "; cin >> angle;

            while ((cin.good() != true) || (cin.peek() != '\n') || (angle > 90) || (angle < 0))
            {

                cout << "\nYou have entered an invalid value\n" << endl;
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cout << "Try again =>  ";
                cout << "Angle between hypotenuse and leg = "; cin >> angle;
            }

            //Вывод Результата по Синусам Косинусам
            leg = hyp * cos(angle * M_PI / 180.);
            cout << "Result : " << setprecision(2) << fixed << "leg1 = " << leg << "\n";
            leg2 = hyp * sin(angle * M_PI / 180.);
            cout << "Result : " << setprecision(2) << fixed << "leg2 = " << leg2 << "\n";
        }
        //2 Второй вариант решения задачи путём теоремы пифагора
        else
        {
            //Ввод и проверка длины гипотенузы
            cout << "Hypotenuse = "; cin >> hyp;
            while ((cin.good() != true) || (cin.peek() != '\n') || (hyp < 0))
            {
                cout << "\nYou have entered an invalid value\n" << endl;
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cout << "Try again =>  ";
                cout << "Hypotenuse = "; cin >> hyp;

            }


            //Ввод и проверка длины катета
            cout << "Leg = "; cin >> leg;
            while ((cin.good() != true) || (cin.peek() != '\n') || (leg < 0) || (leg > hyp)) {

                cout << "\nYou have entered an invalid value\n" << endl;
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cout << "Try again =>  ";
                cout << "Leg = "; cin >> leg;
            }
            //Вывод Результата по ПИфагору
            cout << "Result : " << sqrt(hyp * hyp - leg * leg) << "\n";

            cout << "ans = ", cin >> ans;
            while ((cin.good() != true) || (cin.peek() != '\n')) {

                cout << "\nYou have entered an invalid value\n" << endl;
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cout << "Try again =>  ";
                cout << "Ans = "; cin >> ans;
            cin >> ans;count<<"Would you like to try again(Print Y or y if you want )"
            }
        }

    } while (ans == "Y" || ans == "y");

}












