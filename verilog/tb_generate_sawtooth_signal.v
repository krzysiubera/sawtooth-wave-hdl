module tb_generate_sawtooth_signal;

wire [15:0] output;
reg clk;
reg reset;

initial begin
    $from_myhdl(
        clk,
        reset
    );
    $to_myhdl(
        output
    );
end

generate_sawtooth_signal dut(
    output,
    clk,
    reset
);

endmodule
