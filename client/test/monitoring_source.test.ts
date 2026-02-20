import { MonitoringSourcesService, OpenAPI, SourceType } from '..';

describe('MonitoringSourcesService', () => {
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

  it('should create, get, update, and delete a monitoring source', async () => {
    // Create
    const createdSource = await MonitoringSourcesService.createMonitoringSourceMonitoringSourcesPost({
      name: 'Test Source',
      type: SourceType.WEBSITE,
      url: 'https://example.com',
    });
    expect(createdSource).toBeDefined();
    expect(createdSource.name).toEqual('Test Source');
    const sourceId = createdSource._id!;

    // Get
    const fetchedSource = await MonitoringSourcesService.getMonitoringSourceMonitoringSourcesIdGet(sourceId);
    expect(fetchedSource).toBeDefined();
    expect(fetchedSource.name).toEqual('Test Source');

    // Get all by user
    const sources = await MonitoringSourcesService.getMonitoringSourcesByUserMonitoringSourcesGet();
    expect(sources).toBeDefined();
    expect(sources.length).toBeGreaterThan(0);

    // Update
    const updatedSource = await MonitoringSourcesService.updateMonitoringSourceMonitoringSourcesIdPut(sourceId, {
      name: 'Updated Test Source',
    });
    expect(updatedSource).toBeDefined();
    expect(updatedSource.name).toEqual('Updated Test Source');

    // Delete
    await MonitoringSourcesService.deleteMonitoringSourceMonitoringSourcesIdDelete(sourceId);

    // Verify deletion
    await expect(MonitoringSourcesService.getMonitoringSourceMonitoringSourcesIdGet(sourceId)).rejects.toThrow();
  });
});
