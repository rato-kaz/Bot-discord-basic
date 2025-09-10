import discord
from discord.ext import commands
import requests
import os
from io import BytesIO

HF_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

class StableDiffusion(commands.Cog):
    def __init__(self, bot):  # Fixed: proper __init__ syntax
        self.bot = bot

    @commands.command(name="imagine", help="Tạo ảnh từ prompt bằng Stable Diffusion XL")
    async def imagine(self, ctx, *, prompt: str):
        # Send initial message
        initial_msg = await ctx.send(f"🎨 Đang tạo ảnh cho prompt: `{prompt}` ... Vui lòng chờ!")
        
        try:
            # Make the API request
            response = requests.post(
                HF_API_URL,
                headers=HEADERS,
                json={"inputs": prompt},
                timeout=30  # Add timeout to prevent hanging
            )
            
            if response.status_code != 200:
                await initial_msg.edit(content=f"❌ Lỗi: {response.text}")
                return
            
            # Check if response has content
            if not response.content:
                await initial_msg.edit(content="❌ Lỗi: Không nhận được dữ liệu ảnh từ API")
                return
            
            # Save image to memory buffer
            image_bytes = BytesIO(response.content)
            file = discord.File(fp=image_bytes, filename="stable_diffusion_result.png")
            
            # Send the generated image
            await ctx.send(f"✅ Ảnh được tạo với prompt: `{prompt}`", file=file)
            
            # Delete the "waiting" message
            await initial_msg.delete()
            
        except requests.exceptions.Timeout:
            await initial_msg.edit(content="❌ Lỗi: API timeout - thời gian chờ quá lâu")
        except requests.exceptions.RequestException as e:
            await initial_msg.edit(content=f"❌ Lỗi kết nối: {str(e)}")
        except discord.errors.HTTPException as e:
            await initial_msg.edit(content=f"❌ Lỗi Discord: {str(e)}")
        except Exception as e:
            await initial_msg.edit(content=f"❌ Lỗi không xác định: {str(e)}")

# For discord.py 2.0+
async def setup(bot):
    await bot.add_cog(StableDiffusion(bot))

# For discord.py 1.x (if you're using older version)
# def setup(bot):
#     bot.add_cog(StableDiffusion(bot))