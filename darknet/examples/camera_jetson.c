//
// Created by tonycalvez on 17/01/2020.
//

//#include <bits/stdc++.h>
//using namespace std;
//
//void camera_starter(){
//    char filename[100];
//    cout << "Enter file name to compile ";
//    cin.getline(filename, 100);
//
//    // Build command to execute.  For example if the input
//    // file name is a.cpp, then str holds "gcc -o a.out a.cpp"
//    // Here -o is used to specify executable file name
//    string str = "gcc ";
//    str = str + " -o a.out " + filename;
//
//    // Convert string to const char * as system requires
//    // parameter of type const char *
//    const char *command = str.c_str();
//
//    cout << "Compiling file using " << command << endl;
//    system(command);
//
//    cout << "\nRunning file ";
//    system("./a.out");
//
//    return 0;
//};

// A C++ program that compiles and runs another C++
// program
#include <bits/stdc++.h>
using namespace std;
int main ()
{
    char filename[100];
    cout << "JetsonCameraExporter";
    cin.getline(filename, 100);

    // Build command to execute.  For example if the input
    // file name is a.cpp, then str holds "gcc -o a.out a.cpp"
    // Here -o is used to specify executable file name
    string str = "gst-launch-1.0 -v nvarguscamerasrc ! 'video/x-raw(memory:NVMM), format=NV12, width=1920, height=1080, framerate=30/1' ! nvvidconv ! 'video/x-raw, width=640, height=480, format=I420, framerate=30/1' ! videoconvert ! identity drop-allocation=1 ! 'video/x-raw, width=640, height=480, format=RGB, framerate=30/1' ! v4l2sink device=/dev/video2";
    str = str + " -o a.out " + filename;

    // Convert string to const char * as system requires
    // parameter of type const char *
    const char *command = str.c_str();

    cout << "Compiling file using " << command << endl;
    system(command);

    cout << "\nRunning file ";
    system("./a.out");

    return 0;
}