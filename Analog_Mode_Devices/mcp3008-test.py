#!/usr/bin/env python3
import time
import argparse
from gpiozero import MCP3008

def test_channel(channel, duration=10, interval=0.5):
    """Test a specific MCP3008 ADC channel.
    
    Args:
        channel (int): Channel number (0-7) to test
        duration (int): Test duration in seconds
        interval (float): Interval between readings in seconds
    """
    try:
        # Initialize the MCP3008 ADC for the specified channel
        adc = MCP3008(channel=channel)
        
        print(f"Testing MCP3008 channel {channel} for {duration} seconds...")
        print(f"{'Time (s)':8} {'Raw (0-1)':10} {'Voltage (V)':12}")
        print("-" * 32)
        
        start_time = time.time()
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            raw_value = adc.value
            voltage = raw_value * 3.3  # Assuming 3.3V reference
            
            print(f"{elapsed:8.2f} {raw_value:10.3f} {voltage:12.3f}")
            time.sleep(interval)
            
        print(f"\nChannel {channel} test completed.\n")
        
    except Exception as e:
        print(f"Error testing channel {channel}: {e}")

def test_all_channels(duration_per_channel=5, interval=0.5):
    """Test all MCP3008 ADC channels sequentially.
    
    Args:
        duration_per_channel (int): Test duration per channel in seconds
        interval (float): Interval between readings in seconds
    """
    print("Testing all MCP3008 channels...")
    for channel in range(8):
        test_channel(channel, duration_per_channel, interval)

def main():
    """Main function to run MCP3008 ADC tests."""
    parser = argparse.ArgumentParser(description='Test MCP3008 ADC channels')
    parser.add_argument('--channel', type=int, choices=range(8), 
                        help='Channel to test (0-7). If not specified, all channels will be tested.')
    parser.add_argument('--duration', type=int, default=10,
                        help='Test duration in seconds (default: 10)')
    parser.add_argument('--interval', type=float, default=0.5,
                        help='Interval between readings in seconds (default: 0.5)')
    
    args = parser.parse_args()
    
    try:
        print("MCP3008 ADC Test")
        print("================")
        
        if args.channel is not None:
            test_channel(args.channel, args.duration, args.interval)
        else:
            test_all_channels(args.duration, args.interval)
            
        print("Test completed successfully.")
        
    except KeyboardInterrupt:
        print("\nTest interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
