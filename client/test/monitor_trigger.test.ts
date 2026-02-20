import { MonitorTriggersService, OpenAPI } from '..';

describe('MonitorTriggersService', () => {
  beforeAll(() => {
    OpenAPI.BASE = 'http://localhost:8000';
    const payload = {
      sub: 'test-user-id-123',
      roles: ['admin'],
    };
    const header = Buffer.from(JSON.stringify({ alg: 'none' })).toString('base64url');
    const claims = Buffer.from(JSON.stringify(payload)).toString('base64url');
    const token = `${header}.${claims}.`;
    OpenAPI.TOKEN = token;
  });

  it('should create, get and delete a monitor trigger', async () => {
    const createdTrigger = await MonitorTriggersService.createMonitorTriggerMonitorTriggersPost({
      language: 'en',
    });
    expect(createdTrigger).toBeDefined();
    expect(createdTrigger.language).toEqual('en');

    // Get
    const fetchedTrigger = await MonitorTriggersService.getMonitorTriggerMonitorTriggersGet();
    expect(fetchedTrigger).toBeDefined();
    expect(fetchedTrigger.language).toEqual('en');

    // Delete
    await MonitorTriggersService.deleteMonitorTriggerMonitorTriggersDelete();
    
    // Verify deletion by trying to get it again, expecting a 404
    await expect(MonitorTriggersService.getMonitorTriggerMonitorTriggersGet()).rejects.toThrow();
  });
});
