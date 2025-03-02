from config.bot_setup import bot

GUILD_ID = 1341420376013668402
BASE_VOICE_CHANNEL_ID = 1345163969639219362

team_counters = {}

@bot.event
async def on_voice_state_update(member, before, after):
    guild = bot.get_guild(GUILD_ID)

    if after.channel and after.channel.id == BASE_VOICE_CHANNEL_ID:
        category = after.channel.category

        next_team_number = team_counters.get(guild.id, 1)
        team_counters[guild.id] = next_team_number + 1

        new_channel = await guild.create_voice_channel(
            name=f"💀 Team {next_team_number}",
            category=category,
            user_limit=4
        )

        await member.move_to(new_channel)

        print(f"✅ Created channel {new_channel.name} for {member.display_name}")

    if before.channel and before.channel != after.channel:
        if before.channel.id != BASE_VOICE_CHANNEL_ID and len(before.channel.members) == 0:
            await before.channel.delete()
            print(f"🗑 Deleted empty channel {before.channel.name}")