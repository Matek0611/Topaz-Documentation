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
    Objects are fully managed by the garbage collector. Only external pointers should be checked.

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

## Run Modes

=== ":material-script-text-outline: Module run"
    <div class="window">
        <div class="titlebar">Terminal</div>
        <div class="body">
            <div class="window-line">__project&gt;__&nbsp;topaz -m fib.tpz 3 10</div>
            <div class="window-line">Fibonacci sequence from the 3rd to 10th term:</div>
            <div class="window-line">1&emsp;2&emsp;3&emsp;5&emsp;8&emsp;13&emsp;21&emsp;34</div>
            <div class="window-line">__project&gt;__&nbsp;<span class="cursor"></span></div>
        </div>
    </div>

=== ":material-sticker-text-outline: Inline code"
    <div class="window">
        <div class="titlebar">Terminal</div>
        <div class="body">
            <div class="window-line">__project&gt;__ topaz -c "var i := 100; while i do begin Print(i * 2, ' '); i -= 1; end; PrintLine();"</div>
            <div class="window-line">&nbsp;</div>
            <div class="window-line">100&emsp;99&emsp;98&emsp;97&emsp;96&emsp;95&emsp;94&emsp;93&emsp;92&emsp;91&emsp;90&emsp;89&emsp;88&emsp;87&emsp;86&emsp;85&emsp;84&emsp;83&emsp;82&emsp;81&emsp;80&emsp;79&emsp;78&emsp;77&emsp;76&emsp;75&emsp;74&emsp;73&emsp;72&emsp;71&emsp;70&emsp;69&emsp;68&emsp;67&emsp;66&emsp;65&emsp;64&emsp;63&emsp;62&emsp;61&emsp;60&emsp;59&emsp;58&emsp;57&emsp;56&emsp;55&emsp;54&emsp;53&emsp;52&emsp;51&emsp;50&emsp;49&emsp;48&emsp;47&emsp;46&emsp;45&emsp;44&emsp;43&emsp;42&emsp;41&emsp;40&emsp;39&emsp;38&emsp;37&emsp;36&emsp;35&emsp;34&emsp;33&emsp;32&emsp;31&emsp;30&emsp;29&emsp;28&emsp;27&emsp;26&emsp;25&emsp;24&emsp;23&emsp;22&emsp;21&emsp;20&emsp;19&emsp;18&emsp;17&emsp;16&emsp;15&emsp;14&emsp;13&emsp;12&emsp;11&emsp;10&emsp;9&emsp;8&emsp;7&emsp;6&emsp;5&emsp;4&emsp;3&emsp;2&emsp;1</div>
            <div class="window-line">__project&gt;__&nbsp;<span class="cursor"></span></div>
        </div>
    </div>

=== ":material-arrow-right-drop-circle-outline: REPL"
    <div class="window">
        <div class="titlebar">Terminal</div>
        <div class="body">
            <div class="window-line">__project&gt;__&nbsp;topaz</div>
            <div class="window-line">__&gt;&gt;&gt;__&nbsp;PrintLine(|val TOPAZ_NATIVE|);</div>
            <div class="window-line">true</div>
            <div class="window-line">__&gt;&gt;&gt;__&nbsp;var x := 1;</div>
            <div class="window-line">__...__&nbsp;while x < 20 do </div>
            <div class="window-line">__...__&nbsp;&nbsp;PrintLine(x *= 2);</div>
            <div class="window-line">__...__&nbsp;<span class="cursor"></span></div>
        </div>
    </div>

=== ":material-text-box-edit-outline: Text-based IDE"
    <div class="window">
        <div class="titlebar">Terminal</div>
        <div class="body">
            <div class="window-line">_Coming soon..._</div>
        </div>
    </div>
    

## Blog Posts
