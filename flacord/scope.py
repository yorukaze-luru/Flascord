
identify = ["identify"]
email = ["email"]
connections = ["connections"]
guilds = ["guilds"]
guilds_join = ["guilds.join"]
guilds_members_read = ["guilds.members.read"]
gdm_join = ["gdm.join"]
rpc = ["rpc"]
rpc_notifications_read = ["rpc.notifications.read"]
rpc_voice_read = ["rpc.voice.read"]
rpc_voice_write = ["rpc.voice.write"]
rpc_activities_write = ["rpc.activities.write"]
bot = ["bot"] 
webhook_incoming = ["webhook.incoming"] 
messages_read = ["messages.read"] 
applications_builds_upload = ["applications.builds.upload"] 
applications_builds_read = ["applications.builds.read"] 
applications_commands = ["applications.commands"] 
applications_store_update = ["applications.store.update"] 
applications_entitlements = ["applications.entitlements"] 
activities_read = ["activities.read"] 
activities_write = ["activities.write"] 
relationships_read = ["relationships.read"] 
voice = ["voice"]
dm_channels_read = ["dm_channels.read"]
role_connections_write = ["role_connections.write"]
applications_commands_permissions_update = ["applications.commands.permissions.update"]

none = []
basic = identify + guilds
invite_bot = bot + applications_commands
all = identify + email + connections + guilds + guilds_join + guilds_members_read + gdm_join + rpc + rpc_notifications_read + rpc_voice_read + rpc_voice_write + rpc_activities_write + bot + webhook_incoming + messages_read + applications_builds_upload + applications_builds_read + applications_commands + applications_store_update + applications_entitlements + activities_read + activities_write + relationships_read + voice + dm_channels_read + role_connections_write + applications_commands_permissions_update



