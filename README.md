Image Thresholding with C++ (DLL) + Python + OpenCV

This project demonstrates how to accelerate image processing using a C++ DLL integrated with Python (ctypes) and OpenCV.

Project Objective

Demonstrate how to:

integrate C++ with Python
accelerate pixel-by-pixel operations
work with shared memory (zero-copy)

This is a didactic implementation. OpenCV already provides a built-in threshold function (cv.threshold).

Operation Implemented

The implemented operation is a binary threshold, where:

pixels above a threshold (t) → white (255)
pixels below or equal to the threshold → black (0)



Project Structure
/project
│── main.py          # uses C++ DLL
│── test.py          # uses OpenCV (cv.threshold)
│── opencvdll.dll
│── sunflower.jpg



1. The C++ DLL

The C++ DLL in the project was compiled with code blocks from the following source following code:



extern "C" \_\_declspec(dllexport)
void threshold\_custom(
unsigned char\* img, // array of bytes (0–255)
int rows,
int cols,
unsigned char t // threshold (0–255)
)
{
int n = rows \* cols;
for (int i = 0; i < n; ++i)
img\[i] = img\[i] > t ? 255 : 0;
}



Compilation Options

You can use:

Code::Blocks (recommended)
MinGW (g++)
Visual Studio
In Code::Blocks:
Create a Dynamic Link Library project
Paste the code into a .cpp file
Build the project

The DLL will be generated at:

bin/Debug/mylib.dll

Copy this file to the project root folder.



2. Install Dependencies
pip install opencv-python numpy
3. Python Version

Recommended:

Python 3.10 (64-bit)



3. Python Scripts

There are two scripts:

main.py: implements the threshold using the C++ DLL
test.py: implements the threshold using OpenCV (cv.threshold)

Both scripts output execution time to the command line, allowing performance comparison.



4. How to Run

Run the scripts separately:



python main.py
python test.py



5. Expected Output
sunflower\_threshold.png
sunflower\_threshold\_opencv.png



Example timings:

DLL:        0.122 ms
OpenCV:     0.039 ms



Both outputs produce:


black and white (bicolor) result


Performance Discussion

During testing, OpenCV may perform as fast or faster than the custom C++ implementation.

Why is OpenCV so fast?

OpenCV is heavily optimized and uses low-level CPU features:

SIMD (Single Instruction, Multiple Data)

SIMD allows a CPU to process multiple data elements in a single instruction.

Instead of:

1 pixel per operation

SIMD enables:

8, 16, or 32 pixels per operation
SSE (Streaming SIMD Extensions)
introduced by Intel
operates on 128-bit registers
processes multiple values in parallel
widely supported on modern CPUs
AVX (Advanced Vector Extensions)
operates on 256-bit (or larger) registers
processes more data per instruction
significantly increases throughput
Additional OpenCV Optimizations
branchless operations (avoids costly if conditions)
memory alignment and cache optimization
optional multithreading
highly tuned low-level implementations
Why the C++ DLL is Still Important

The custom implementation:

is simple and efficient
avoids Python overhead
demonstrates direct memory manipulation
is ideal for learning and custom pipelines

OpenCV, however, is a production-grade library optimized over many years.



6. Technologies Used
C++ (DLL)
Python (ctypes)
OpenCV
NumPy
7. Flexibility vs Low-Level Control

While OpenCV provides highly optimized and easy-to-use functions, it operates at a higher level of abstraction.

Typical OpenCV workflow:

blur → threshold → edge detection

This may result in:

multiple passes over the image
additional memory allocations
limited control over execution
Custom C++ (DLL Approach)

Using a custom C++ implementation allows:

full control over memory access
custom pixel-wise logic
fusion of multiple operations into a single loop
implementation of algorithms not available in OpenCV

Example:

single loop → threshold + filtering + transformation

This level of control is not directly achievable with standard OpenCV calls.

OpenCV Approach

OpenCV is:

highly optimized (SIMD, AVX, multithreading)
reliable and production-ready
ideal for standard image processing tasks

However, it is limited to:

its existing API
predefined operations
Key Insight
OpenCV optimizes what is common; C++ allows you to optimize what is unique.
When to Use Each
Use OpenCV for:
standard operations
rapid development
maximum performance with minimal effort
Use custom C++ (DLL) for:
specialized algorithms
experimental pipelines
fine-grained performance tuning
combining multiple operations efficiently

