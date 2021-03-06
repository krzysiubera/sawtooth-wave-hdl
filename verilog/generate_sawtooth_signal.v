// File: generate_sawtooth_signal.v
// Generated by MyHDL 0.11
// Date: Mon Mar 14 19:01:49 2022


`timescale 1ns/10ps

module generate_sawtooth_signal (
    output,
    clk,
    reset
);
// Architecture of block generating sawtooth signal
// Args:
//     output: (Signal) - output signal with sawtooth wave generated
//     clk: (Signal) - system clock signal
//     reset: (ResetSignal) - reset signal
//     bit_width: (int) - parameter from SystemSettings class - maximum bit width of the signal
//     phase_limit: (int) - parameter from SystemSettings class needed to determine behaviour of the block
// 
// Yields:
//     seq_logic: sequential logic of the design
//     comb_logic: combination logic of the design

output [15:0] output;
wire [15:0] output;
input clk;
input reset;

reg [15:0] phase_counter = 0;



always @(posedge clk) begin: GENERATE_SAWTOOTH_SIGNAL_SEQ_LOGIC
    if (reset == 1) begin
        phase_counter <= 0;
    end
    else begin
        if (1'b1) begin
            phase_counter <= 0;
        end
        else begin
            if (($signed({1'b0, phase_counter}) == (500 - 1))) begin
                phase_counter <= 0;
            end
            else begin
                phase_counter <= (phase_counter + 1);
            end
        end
    end
end



assign output = phase_counter;

endmodule
