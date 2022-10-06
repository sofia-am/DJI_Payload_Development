################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Utilities/Components/lsm303dlhc/lsm303dlhc.c 

OBJS += \
./Utilities/Components/lsm303dlhc/lsm303dlhc.o 

C_DEPS += \
./Utilities/Components/lsm303dlhc/lsm303dlhc.d 


# Each subdirectory must supply rules for building sources it contributes
Utilities/Components/lsm303dlhc/%.o: ../Utilities/Components/lsm303dlhc/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU GCC Compiler'
	@echo $(PWD)
	arm-none-eabi-gcc -mcpu=cortex-m4 -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16 -DSTM32 -DSTM32F4 -DSTM32F411VETx -DSTM32F411E_DISCO -DDEBUG -DSTM32F411xE -DUSE_HAL_DRIVER -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/ili9325" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/s25fl512s" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/cs43l22" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/ili9341" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/ampire480272" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/n25q512a" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/s5k5cag" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/mfxstm32l152" -I"C:/Users/sofia/workspace/3er_intento/CMSIS/device" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/n25q128a" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/ts3510" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/st7735" -I"C:/Users/sofia/workspace/3er_intento/HAL_Driver/Inc/Legacy" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/lis302dl" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/otm8009a" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/stmpe1600" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/Common" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/ov2640" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/l3gd20" -I"C:/Users/sofia/workspace/3er_intento/Utilities/STM32F411E-Discovery" -I"C:/Users/sofia/workspace/3er_intento/HAL_Driver/Inc" -I"C:/Users/sofia/workspace/3er_intento/Utilities" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/stmpe811" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/lis3dsh" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/wm8994" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Fonts" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/n25q256a" -I"C:/Users/sofia/workspace/3er_intento/inc" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/ls016b8uy" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/ft6x06" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/exc7200" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/st7789h2" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/ampire640480" -I"C:/Users/sofia/workspace/3er_intento/Utilities/Components/lsm303dlhc" -I"C:/Users/sofia/workspace/3er_intento/CMSIS/core" -O0 -g3 -Wall -fmessage-length=0 -ffunction-sections -c -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


