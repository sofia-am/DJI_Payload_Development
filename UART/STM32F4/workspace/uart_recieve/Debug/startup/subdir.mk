################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
S_SRCS += \
../startup/startup_stm32f411xe.s 

OBJS += \
./startup/startup_stm32f411xe.o 


# Each subdirectory must supply rules for building sources it contributes
startup/%.o: ../startup/%.s
	@echo 'Building file: $<'
	@echo 'Invoking: MCU GCC Assembler'
	@echo $(PWD)
	arm-none-eabi-as -mcpu=cortex-m4 -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16 -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/ili9325" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/s25fl512s" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/cs43l22" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/ili9341" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/ampire480272" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/n25q512a" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/s5k5cag" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/mfxstm32l152" -I"C:/Users/sofia/workspace/uart_recieve/CMSIS/device" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/n25q128a" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/ts3510" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/st7735" -I"C:/Users/sofia/workspace/uart_recieve/HAL_Driver/Inc/Legacy" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/lis302dl" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/otm8009a" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/stmpe1600" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/Common" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/ov2640" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/l3gd20" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/STM32F411E-Discovery" -I"C:/Users/sofia/workspace/uart_recieve/HAL_Driver/Inc" -I"C:/Users/sofia/workspace/uart_recieve/Utilities" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/stmpe811" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/lis3dsh" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/wm8994" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Fonts" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/n25q256a" -I"C:/Users/sofia/workspace/uart_recieve/inc" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/ls016b8uy" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/ft6x06" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/exc7200" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/st7789h2" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/ampire640480" -I"C:/Users/sofia/workspace/uart_recieve/Utilities/Components/lsm303dlhc" -I"C:/Users/sofia/workspace/uart_recieve/CMSIS/core" -g -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


