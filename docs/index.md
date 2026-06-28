---
hide:
  - footer
  - navigation
  - toc
template: home_page.html
---

# Home

## Key Features

<div class="grid cards" markdown>

-   :material-laptop: __Cross-Platform__<br>
    Build scripts, TUI, GUI apps and games for Windows, macOS, and Linux from the unchanged source.

-   :material-code-tags: __Comprehensible Syntax__<br>
    You can read the code like a manual. No unnecessary symbols or strange keywords.

-   :material-shape-outline: __Composition-Oriented__<br>
    Instead of classes and interfaces, there are components and features. Component has state and relies on features that describe its behavior. 

-   :material-button-cursor: __Build-in GUI Library__<br>
    You don't have to install third-party libraries to create desktop apps. Topaz Core GUI allows you to design native windows and widgets.

-   :material-function: __CPU/GPU Native & External Functions__<br>
    Import functions from external libraries or implement ones compiled to machine code and called in JIT mode or on the GPU.

-   :material-abacus: __Async Tasks__<br>
    Declare asynchronous functions and run them in parallel. Inbuilt thread pool and async queue workers will handle everything for you.

-   :material-shield-half-full: __Memory Safety__<br>
    Objects are fully managed by the garbage collector. Only external pointers must be checked.

-   :material-file-cog: __Preprocessor__<br>
    You can create source code that may be optimized before compilation.

</div>

## Elegant Code

=== "Factorial"
    ```topaz linenums="1"
    function Factorial(n: LongNatural): LongNatural;
        Result := 1;
        for var i := 2..n do
            Result *= i;
    end;

    const number = 15;
    PrintLine("${number}! = ${Factorial(number)}");
    ```

=== "Variadic"
    ```topaz linenums="1"
    @VarArgs
    function DoV();
        PrintLine(VarArgs[0]);
    end;

    DoV(1, 2, 3);

    @MapArgs
    function DoM();
        PrintLine(MapArgs['X'] * 10);
    end;

    DoM(x: 5);

    @VarArgs
    @MapArgs
    function DoAll();
        PrintLine(VarArgs[0], MapArgs['A'], MapArgs['B'], VarArgs[1]);
    end;

    DoAll(10, 4.5, a: 5, b: 'test');
    ```

=== "Asynchronous calls"
    ```topaz linenums="1"
    @Async
    function NewPrint(p: UnicodeString);
        var i := 1000;
        while i do begin
            Print(p, ': ', i, ' ');
            i -= 1;
        end;
        PrintLine();
    end;

    NewPrint('A'); 
    NewPrint('B');
    NewPrint('C');
    ```

=== "Preprocessor & external functions"
    ```topaz linenums="1"
    |if def(Windows)|
        @External(Name := 'ReadFileW', Library := 'kernel32', Delayed := true)
        function ReadFile(hFile: TFileHandle, lpBuffer: Pointer,
            nNumberOfBytesToRead: Natural, ref lpNumberOfBytesRead: Natural,
            lpOverlapped: Pointer): Boolean;

        @External('user32')
        function MessageBoxW(hwnd: LongNatural, (lpText, lpCaption): CWideString,
            uType: Natural): Integer;

        MessageBoxW(0, 'Hello!', 'Topaz', $41);
    |end|

    @External(
        |if def(Windows)|
            'msvcrt'
        |else if def(macOS)|
            'libSystem'
        |else|
            'c'
        |end|
    )
    @VarArgs
    function printf(const format: CString): Integer;

    printf("x = %d + %s %f\n", 6, CString('me'), 8.5); 
    ```

=== "Native"
    ```topaz linenums="1"
    @Native
    function FastAvg(Numbers: array of Double): Double;
        Result := 0;

        for var num in Numbers do
            Result += num;

        Result /= Numbers.Size();
    end;

    Print(FastAvg([4, 5.6, 2.5]));
    ```

=== "Features & components"
    ```topaz linenums="1"
    type of
        IShowable = feature
            use Data: LongInteger;

            method Show(): String;
                Result := "${Self.Data}";
            end;
        end;

        IMultiple = feature
            use Data: LongInteger;

            method Multiply(X: Integer): LongInteger;
                Result := Self.Data * X;
            end;
        end;

        Container = component(IShowable, IMultiple)
            private var Data: LongInteger;

            constructor ();
                Self.Data := 0;
            end;

            destructor ();
                Self.Data := -1;
            end;

            constructor New(Data: LongInteger);
                Self.Data := Data;
            end;
        end;
    end;

    const C = Container.New(20);
    PrintLine(C.Show());
    PrintLine(C.Multiply(2));
    ```

=== "Topaz GUI framework"
    ```topaz linenums="1"
    use (Application, GUIColor) of Core.GUI;
  
    const Main := Application.NewWindow();
    Main.Color := GUIColor($451388FF);

    Application.MainWindow := Main;
    Application.Title := 'Test';
    Application.Run();
    ```
