#include "stm32f4xx_hal.h"

void Init_OnBoard_LEDs(void);
void Delay_ms(volatile int time_ms);
int main(void)
{
  Init_OnBoard_LEDs();
  while(1)
  {
  HAL_GPIO_TogglePin(GPIOD,GPIO_PIN_12|GPIO_PIN_13|GPIO_PIN_14|GPIO_PIN_15);
  Delay_ms(1000);
  }
}

void Init_OnBoard_LEDs(void)
{
   __HAL_RCC_GPIOD_CLK_ENABLE();
  GPIO_InitTypeDef BoardLEDs;
  BoardLEDs.Mode = GPIO_MODE_OUTPUT_PP;
  BoardLEDs.Pin = GPIO_PIN_12|GPIO_PIN_13|GPIO_PIN_14|GPIO_PIN_15;
  HAL_GPIO_Init(GPIOD, &BoardLEDs);
}
void Delay_ms(volatile int time_ms)
{
        int j;
        for(j = 0; j < time_ms*4000; j++)
            {}  /* excute NOP for 1ms */
}
